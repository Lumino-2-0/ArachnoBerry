"""
 _______       _            _     _          ______        _                 _ 
(_______)     (_)       _  (_)   | |        (____  \      (_)               | |
 _______  ____ _  ___ _| |_ _  __| |_____    ____)  ) ____ _ _____ ____   __| |
|  ___  |/ ___) |/___|_   _) |/ _  | ___ |  |  __  ( / ___) (____ |  _ \ / _  |
| |   | | |   | |___ | | |_| ( (_| | ____|  | |__)  ) |   | / ___ | | | ( (_| |
|_|   |_|_|   |_(___/   \__)_|\____|_____)  |______/|_|   |_\_____|_| |_|\____|
    
Auteur: Sam BERTAUX (Lumastor)(sam.bertaux.pro@gmail.com / lumino110908@gmail.com) 
TEST.py(Ɔ) 2026
Description : Saisissez la description puis « Tab »
Créé le :  mardi 17 mars 2026 à 10:39:43 
Dernière modification : mardi 31 mars 2026 à 10:43:02
"""

# ---------------------------------------------------------
# IMPORTATION DES MODULES
# ---------------------------------------------------------
# network  -> gestion du Wi-Fi
# socket   -> communication réseau (serveur web)
# machine  -> accès au matériel (GPIO, LED…)
# time     -> temporisations
# ---------------------------------------------------------

import network
import socket
from machine import Pin
import time
from patedeporc import Servo_test, forward, backward

# ---------------------------------------------------------
# CONFIGURATION DE LA LED INTERNE
# ---------------------------------------------------------
# Sur le Raspberry Pi Pico W, la LED intégrée
# est accessible via le nom spécial "LED"
# ---------------------------------------------------------

led = Pin("LED", Pin.OUT)   # OUT = sortie (on contrôle la LED)


# ---------------------------------------------------------
# CONFIGURATION DU WIFI EN MODE POINT D'ACCES (AP)
# ---------------------------------------------------------
# Le Pico W va créer SON PROPRE réseau Wi-Fi
# Les élèves pourront s’y connecter directement
# ---------------------------------------------------------

ssid = "PanierPianoPanierPiano"           # Nom du réseau Wi-Fi
password = "labeillecoule"       # Mot de passe (8 caractères mini)

ap = network.WLAN(network.AP_IF)  # Création d’un objet Wi-Fi en mode AP
ap.active(True)                    # Activation du Wi-Fi
ap.config(essid=ssid, password=password)

print("Wi-Fi actif")
print("Nom du réseau :", ssid)

# Attendre que le Wi-Fi soit prêt
while not ap.active():
    time.sleep(0.1)

print("Adresse IP du Pico :", ap.ifconfig()[0])


# ---------------------------------------------------------
# FONCTION QUI GENERE LA PAGE HTML
# ---------------------------------------------------------
# Cette fonction construit une page web sous forme
# de TEXTE (chaîne de caractères)
# ---------------------------------------------------------

def webpage():

    if led.value():
        state = "ON"
    else:
        state = "OFF"

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Controle Araignee Pico</title>

<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
body {{
    font-family: Arial;
    background: #111;
    color: white;
    text-align: center;
}}

h1 {{
    margin-top: 20px;
}}

.container {{
    margin-top: 30px;
}}

button {{
    width: 120px;
    height: 60px;
    margin: 10px;
    font-size: 16px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
}}

.forward {{ background: green; }}
.backward {{ background: red; }}
.left {{ background: blue; }}
.right {{ background: orange; }}

.ledon {{ background: #0f0; color:black; }}
.ledoff {{ background: #555; }}

.status {{
    margin-top: 20px;
    font-size: 14px;
    color: #0f0;
}}
</style>
</head>

<body>

<h1>ArachnoBerry controller WebPage</h1>
<p>Etat LED : <strong>{state}</strong></p>

<div class="container">
    <button class="forward" onclick="sendCommand('forward')">Avancer</button><br>
    <button class="left" onclick="sendCommand('left')">Gauche</button>
    <button class="right" onclick="sendCommand('right')">Droite</button><br>
    <button class="backward" onclick="sendCommand('backward')">Reculer</button>
</div>

<div>
    <button class="ledon" onclick="sendCommand('ledon')">LED ON</button>
    <button class="ledoff" onclick="sendCommand('ledoff')">LED OFF</button>
</div>

<div>
    <button onclick="sendCommand('servo')">Test Servo</button>
</div>

<div class="status" id="status">
    Manette: non detectee
</div>

<script>
const PICO_IP = window.location.hostname;

// Envoi commande au Pico
function sendCommand(cmd) {{
    fetch(`http://${{PICO_IP}}/cmd?move=${{cmd}}`)
        .catch(err => console.log("Erreur:", err));
}}

// ================= GAMEPAD =================

let gamepadIndex = null;

window.addEventListener("gamepadconnected", (e) => {{
    gamepadIndex = e.gamepad.index;
    document.getElementById("status").innerText = "Manette connectee";
}});

window.addEventListener("gamepaddisconnected", () => {{
    gamepadIndex = null;
    document.getElementById("status").innerText = "Manette deconnectee";
}});

function pollGamepad() {{
    if (gamepadIndex !== null) {{
        const gamepad = navigator.getGamepads()[gamepadIndex];
        if (!gamepad) return;

        let x = gamepad.axes[0];
        let y = gamepad.axes[1];

        if (Math.abs(x) < 0.2) x = 0;
        if (Math.abs(y) < 0.2) y = 0;

        if (y < -0.5) sendCommand("forward");
        else if (y > 0.5) sendCommand("backward");

        if (x < -0.5) sendCommand("left");
        else if (x > 0.5) sendCommand("right");

        if (gamepad.buttons[0].pressed) sendCommand("servo");
        if (gamepad.buttons[1].pressed) sendCommand("ledon");
        if (gamepad.buttons[2].pressed) sendCommand("ledoff");
    }}

    requestAnimationFrame(pollGamepad);
}}

pollGamepad();
</script>

</body>
</html>
"""
    return html


# ---------------------------------------------------------
# CREATION DU SERVEUR WEB
# ---------------------------------------------------------
# Le Pico écoute sur le PORT 80 (HTTP)
# ---------------------------------------------------------

addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]

server = socket.socket()
server.bind(addr)
server.listen(1)

print("Serveur web en attente...")


# ---------------------------------------------------------
# BOUCLE PRINCIPALE
# ---------------------------------------------------------
# Le Pico attend les connexions d’un navigateur
# ---------------------------------------------------------



while True:

    # Attendre un client (navigateur)
    client, addr = server.accept()
    print("Connexion depuis", addr)

    # Lire la requête envoyée par le navigateur
    request = client.recv(1024).decode()
    print("Requête reçue :")
    print(request)

    # -----------------------------------------------------
    # ANALYSE DE L’URL DEMANDEE
    # -----------------------------------------------------

    
    if "forward" in request:
        print("Avancer")
        forward()
            

    elif "backward" in request:
        print("Reculer")
        backward()

    elif "left" in request:
        print("Gauche")
        #turn_left()

    elif "right" in request:
        print("Droite")
        #turn_right()

    elif "ledon" in request:
        led.value(1)
        print("LED allumée")

    elif "ledoff"  in request:
        led.value(0)
        print("LED éteinte")

    elif "servo" in request:
        print("test servomoteurs en cours")
        Servo_test()      
        
    # -----------------------------------------------------
    # ENVOI DE LA PAGE HTML
    # -----------------------------------------------------

    response = webpage()

    # En-tête HTTP obligatoire
    client.send("HTTP/1.1 200 OK\r\n")
    client.send("Content-Type: text/html\r\n\r\n")

    # Contenu de la page
    client.send(response)

    # Fermer la connexion
    client.close()


"""
       _                     _             
      | |                   (_)            
      | |    _   _ _ __ ___  _ _ __   ___  
      | |   | | | |  _   _ \| |  _ \ / _ \ 
      | |___| |_| | | | | | | | | | | (_) |
      |______\____|_| |_| |_|_|_| |_|\___/
    
Auteurs: Sam BERTAUX (Lumastor) + Morgant DESMARS (Dante3ee)
"""
import network
import socket
from machine import Pin
import time

ASYNC = False


led = Pin("LED", Pin.OUT)   # OUT = sortie (on contrôle la LED)


# ---------------------------------------------------------
# CONFIGURATION DU WIFI EN MODE POINT D'ACCES (AP)
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
# GENERE LA PAGE HTML
# ---------------------------------------------------------

def webpage():

    if led.value():
        state = "ON"
    else:
        state = "OFF"
        
    double_state = "ON" if helias.Double else "OFF"

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>ArachnoBerry</title>

<style>
:root {{
    --bg: #0f172a;
    --card: #1e293b;
    --accent: #38bdf8;
    --accent2: #22c55e;
    --danger: #ef4444;
    --text: #e2e8f0;
}}

body {{
    margin:0;
    font-family: 'Segoe UI', system-ui;
    background: radial-gradient(circle at top, #1e293b, #020617);
    color: var(--text);
    text-align:center;
}}

h1 {{
    margin-top:20px;
    font-size:28px;
    letter-spacing:1px;
}}

.card {{
    background: var(--card);
    margin:20px;
    padding:20px;
    border-radius:20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}}

.grid {{
    display:grid;
    grid-template-columns: repeat(3, 1fr);
    gap:10px;
    max-width:300px;
    margin:20px auto;
}}

button {{
    height:70px;
    border:none;
    border-radius:15px;
    font-size:16px;
    font-weight:bold;
    color:white;
    cursor:pointer;
    transition:0.15s;
}}

button:active {{
    transform: scale(0.95);
}}

.forward {{ background: var(--accent2); grid-column:2; }}
.backward {{ background: var(--danger); grid-column:2; }}
.left {{ background: #3b82f6; }}
.right {{ background: #f59e0b; }}

.action {{
    background: var(--accent);
    margin:5px;
    width:140px;
}}

.led-on {{ background:#22c55e; }}
.led-off {{ background:#64748b; }}

.status {{
    margin-top:10px;
    font-size:14px;
    opacity:0.8;
}}

.joystick {{
    width:120px;
    height:120px;
    border-radius:50%;
    background: radial-gradient(circle, #334155, #020617);
    margin:20px auto;
    position:relative;
}}

.stick {{
    width:40px;
    height:40px;
    background: var(--accent);
    border-radius:50%;
    position:absolute;
    top:40px;
    left:40px;
}}

footer {{
    margin-top:30px;
    padding:20px;
    font-size:12px;
    opacity:0.6;
}}

a {{
    color: var(--accent);
    text-decoration:none;
}}
</style>
</head>

<body>

<h1>ArachnoBerry</h1>

<div class="card">
    <p>LED : <strong>{state}</strong></p>
    <p>Mode Double : <strong>{double_state}</strong></p>
</div>

<!-- CONTROLES -->
<div class="card">
    <h3>Contrôles</h3>

    <div class="grid">
        <div></div>
        <button class="forward" onclick="sendCommand('forward')">↑</button>
        <div></div>

        <button class="left" onclick="sendCommand('left')">←</button>
        <div></div>
        <button class="right" onclick="sendCommand('right')">→</button>

        <div></div>
        <button class="backward" onclick="sendCommand('backward')">↓</button>
        <div></div>
    </div>
</div>

<div class="card">
    <h3>Temps de pause</h3>

    <input type="number" id="pauseTime" placeholder="Temps en ms" style="padding:10px; border-radius:10px; border:none; width:200px; font-size:16px;">
    <div style="margin-top:10px;">
        <button class="action" onclick="document.getElementById('pauseTime').value=30">30 ms</button>
        <button class="action" onclick="document.getElementById('pauseTime').value=50">50 ms</button>
        <button class="action" onclick="document.getElementById('pauseTime').value=100">100 ms</button>
        <button class="action" onclick="document.getElementById('pauseTime').value=500">500 ms</button>
    </div>
        
    <button class="action" style="margin-top:10px;" onclick="sendCommand('pauseTime=' + document.getElementById('pauseTime').value)">Envoyer</button>
</div>

<!-- ACTIONS -->
<div class="card">
    <h3>Actions</h3>

    <button class="action" onclick="sendCommand('servo')">Test Servo</button>
    <button class="action" onclick="sendCommand('attack')">Attaque</button>
    <button class="action" onclick="sendCommand('neutral')">Neutre</button>

</div>

<!-- LED -->
<div class="card">
    <h3>LED</h3>

    <button class="action led-on" onclick="sendCommand('ledon')">ON</button>
    <button class="action led-off" onclick="sendCommand('ledoff')">OFF</button>
</div>

<!-- JOYSTICK VISUEL -->
<div class="card">
    <h3>Manette</h3>

    <div class="joystick">
        <div class="stick" id="stick"></div>
    </div>

    <div class="status" id="status">Manette non détectée</div>
</div>

<!-- FOOTER -->
<footer>
    <p>ArachnoBerry Controller</p>
    <p>
        <a href="https://github.com/Lumino-2-0/ArachnoBerry" target="_blank">
        GitHub Project
        </a>
    </p>
    <p>DIY Spider Robot - Pico W - 2026</p>
</footer>

<script>
const PICO_IP = window.location.hostname;

// ================= ANTI-SPAM =================
let lastSentTime = 0;
let lastCommand = "";
const DELAY = 300; //ms

function sendCommand(cmd) {{
    const now = Date.now();

    if (cmd === lastCommand && (now - lastSentTime) < DELAY) return;

    lastSentTime = now;
    lastCommand = cmd;

    fetch(`http://${{PICO_IP}}/cmd?move=${{cmd}}`)
        .catch(()=>{{}});
}}

// ================= GAMEPAD =================
let gamepadIndex = null;

window.addEventListener("gamepadconnected", (e) => {{
    gamepadIndex = e.gamepad.index;
    document.getElementById("status").innerText = "Manette connectée";
}});

window.addEventListener("gamepaddisconnected", () => {{
    gamepadIndex = null;
    document.getElementById("status").innerText = "Manette déconnectée";
}});

const stick = document.getElementById("stick");

function updateStick(x,y){{
    stick.style.left = (40 + x*30) + "px";
    stick.style.top = (40 + y*30) + "px";
}}

function pollGamepad() {{
    if (gamepadIndex !== null) {{
        const gp = navigator.getGamepads()[gamepadIndex];
        if (!gp) return;

        let x = gp.axes[0];
        let y = gp.axes[1];

        // deadzone
        if (Math.abs(x) < 0.2) x = 0;
        if (Math.abs(y) < 0.2) y = 0;

        updateStick(x,y);

        if (y < -0.5) sendCommand("forward");
        else if (y > 0.5) sendCommand("backward");
        else if (x < -0.5) sendCommand("left");
        else if (x > 0.5) sendCommand("right");

        if (gp.buttons[0].pressed) sendCommand("attack"); // bouton A
        if (gp.buttons[2].pressed) sendCommand("servo"); // bouton X
        if (gp.buttons[3].pressed) sendCommand("ledon"); // bouton Y
        if (gp.buttons[1].pressed) sendCommand("ledoff"); // bouton B
        if (gp.buttons[4].pressed) sendCommand("neutral"); // bouton Start

    }}

    requestAnimationFrame(pollGamepad);
}}

pollGamepad();
</script>

</body>
</html>
"""
    return html



# if (ASYNC):
#     from helias_async import backward, forward, turn_right, turn_left, attack, Servo_test 
# else :
#     from helias import backward, forward, turn_right, turn_left, attack, Servo_test 
import helias
from helias import backward, forward, turn_right, turn_left, attack, Servo_test, neutral
print("Modules de contrôle importés")

# ---------------------------------------------------------
# CREATION DU SERVEUR WEB
# ---------------------------------------------------------
# Le Pico écoute sur le PORT 80 (HTTP)
# ---------------------------------------------------------

addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
print("Adresse du serveur :", addr)

server = socket.socket()
print("Socket créé")

server.bind(addr)
print("Socket lié à l'adresse")

server.listen(1)
print("Socket en écoute")

print("Serveur web en attente...")


# ---------------------------------------------------------
# Attend les connexions d’un navigateur
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
        turn_left()

    elif "right" in request:
        print("Droite")
        turn_right()

    elif "ledon" in request:
        led.value(1)
        print("LED allumée")

    elif "ledoff"  in request:
        led.value(0)
        print("LED éteinte")

    elif "servo" in request:
        print("test servomoteurs en cours")
        Servo_test()      
        
    elif "attack" in request:
        print("Attaque !")
        attack()
        
    elif "neutral" in request:
        print("Position neutre")
        neutral()
    
    #Envoi de la pause au code helias avec une variable globale (Time_Pause) pour l'utiliser dans les fonctions de déplacement et d'attaque
    elif "pauseTime=" in request:
        try:
            value = request.split("pauseTime=")[1].split(" ")[0]

            helias.Time_Pause = int(value) / 1000

            print(f"Pause définie à {helias.Time_Pause} secondes")

        except Exception as e:
            print("Erreur pause :", e)
    
        
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


# ArachnoBerry
[dante3ee.fr](https://dante3ee.fr)

> Robot araignée contrôlé en Wi-Fi avec une Raspberry Pi Pico W

![Python](https://img.shields.io/badge/MicroPython-Enabled-blue)
![Hardware](https://img.shields.io/badge/Pico-W-green)
![Status](https://img.shields.io/badge/Project-Active-success)

---

## Description

**ArachnoBerry** est un robot quadrupède (type araignée) contrôlé via une interface web embarquée.
Il fonctionne avec une **Raspberry Pi Pico W** et utilise un driver PWM **PCA9685 (Grove 16 Channels)** pour piloter les servomoteurs.

Le robot peut être contrôlé :

* via navigateur web
* avec une manette (Gamepad API)
* en Wi-Fi direct (mode point d’accès)

---

## Fonctionnalités

* Serveur web embarqué (Pico W)
* Support manette (Gamepad API)
* Interface joystick visuelle
* Contrôle de 4 pattes (8 servos)
* Mode **synchrone** et **asynchrone**
* Mouvements disponibles :

  * Avancer
  * Reculer
  * Tourner gauche / droite
  * Attaque
  * Test servos
* Contrôle LED intégré

---

## Architecture du projet

```
ArachnoBerry/
│
├── main.py                  # Serveur web + contrôleur principal
├── helias.py               # Moteur de mouvement (synchrone)
├── helias_async.py         # Version async (fluide)
├── grove_16_channels_pwm.py # Driver PCA9685 modifié (async)
```

---

## Mode Async vs Sync

Dans `main.py` :

```python
ASYNC = True
```

* `True` -> utilise `helias_async.py` (fluide, non bloquant, plus lent)
* `False` -> utilise `helias.py` (simple, bloquant, plus rapide et reactif)

---

## Matériel requis

* Raspberry Pi Pico W
* Driver PWM PCA9685 (Grove 16 Channels)
* Servomoteurs (x8 recommandé)
* Alimentation externe 5V ⚠️ (obligatoire pour les servos)
* Structure robot (DIY / imprimée 3D)

---

## Installation

1. Flasher MicroPython sur le Pico W
2. Copier les fichiers sur la carte :

   * `main.py`
   * `helias.py`
   * `helias_async.py`
   * `grove_16_channels_pwm.py`
3. Brancher le PCA9685 en I2C :

   * SDA -> GP8
   * SCL -> GP9
4. Alimenter les servos en 5V externe
5. Lancer `main.py`

(Ou téléverser les fichiers et brancher la Pico à une alimentation externe qui ne se connecte pas à celle-ci)

---

## Connexion

* Wi-Fi : A vous de modifiez le code
* Mot de passe : A vous de modifiez le code
* IP : Affichée dans le terminal série

Ensuite ouvrir dans un navigateur :

```
http://<IP_DU_PICO>
```

---

## Contrôles

### Interface Web

* Boutons directionnels
* Actions (attaque, test servo)
* LED ON/OFF

### Manette

* Stick gauche -> déplacement
* Boutons :

  * A → attaque
  * X → test servo
  * Y → LED ON
  * B → LED OFF

---

## Async

Le projet utilise une version custom du driver PCA9685 avec :

```python
async_servo_angle()
```

Avantages :

* mouvements fluides
* multi-servos en parallèle

---

## Limitations

* Serveur HTTP **bloquant**
* Une seule requête à la fois
* Pas de file d’attente de commandes

---

## Améliorations possibles

* Contrôle temps réel (WebSocket)
* Calibration des servos

---

## Auteur

**Sam BERTAUX (Lumastor)**
[lumino110908@gmail.com](mailto:lumino110908@gmail.com)

**Morgant DESMARS (Dante3ee)**
[morgant.desmars@proton.me](mailto:morgant.desmars@proton.me)

---

## Licence

Projet DIY open-source — libre d’utilisation et modification.

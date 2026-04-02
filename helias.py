import time
from machine import I2C, Pin
from grove_16_channels_pwm import Grove16PWM

# ================= INIT =================

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=100_000)
pwm = Grove16PWM(i2c)

# Servo 0 = horizontal (gauche/droite)
# Servo 1 = vertical (haut/bas)

H_CENTER = 90
V_CENTER = 90

h_angle = H_CENTER
v_angle = V_CENTER

def set_leg(h, v):
    pwm.servo_angle(0, h)
    pwm.servo_angle(1, v)

# ================= POSITIONS =================

def neutral():
    set_leg(H_CENTER, V_CENTER)

def lift():
    set_leg(h_angle, 60)   # lever patte

def down():
    set_leg(h_angle, 120)  # poser patte

# ================= MOUVEMENTS =================

def forward():
    global h_angle

    # cycle de marche simple
    lift()
    time.sleep(0.1)

    h_angle = 120
    set_leg(h_angle, 60)
    time.sleep(0.1)

    down()
    time.sleep(0.1)

    h_angle = 60
    set_leg(h_angle, 120)
    time.sleep(0.1)


def backward():
    global h_angle

    lift()
    time.sleep(0.1)

    h_angle = 60
    set_leg(h_angle, 60)
    time.sleep(0.1)

    down()
    time.sleep(0.1)

    h_angle = 120
    set_leg(h_angle, 120)
    time.sleep(0.1)


def turn_left():
    lift()
    time.sleep(0.1)

    set_leg(60, 60)
    time.sleep(0.2)

    down()


def turn_right():
    lift()
    time.sleep(0.1)

    set_leg(120, 60)
    time.sleep(0.2)

    down()


def attack():
    for _ in range(3):
        set_leg(90, 50)
        time.sleep(0.1)
        set_leg(90, 130)
        time.sleep(0.1)

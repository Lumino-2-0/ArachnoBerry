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

def set_leg0(h, v):
    pwm.servo_angle(0, h)
    pwm.servo_angle(1, v)
    
def set_leg1(h, v):
    pwm.servo_angle(2, h)
    pwm.servo_angle(3, v)
    
def set_leg2(h, v):
    pwm.servo_angle(14, h)
    pwm.servo_angle(15, v)

def set_leg3(h, v):
    pwm.servo_angle(12, h)
    pwm.servo_angle(13, v)
    


def Servo_test():
    pwm.servo_angle(0,0)
    pwm.servo_angle(1,0)
    time.sleep(0.5)
    pwm.servo_angle(0,90)
    pwm.servo_angle(1,90)
    time.sleep(0.5)
    pwm.servo_angle(0,180)
    pwm.servo_angle(1,180)
    time.sleep(0.5)

# ================= POSITIONS =================

def neutral():
    set_leg0(H_CENTER, V_CENTER)
    set_leg1(H_CENTER, V_CENTER)
    set_leg2(H_CENTER, V_CENTER)
    set_leg3(H_CENTER, V_CENTER)

def lift():
    set_leg0(h_angle, 60)   # lever patte
    set_leg1(h_angle, 60)   # lever patte
    set_leg2(h_angle, 60)   # lever patte
    set_leg3(h_angle, 60)   # lever patte

def down():
    set_leg0(h_angle, 120)  # poser patte
    set_leg1(h_angle, 120)  # poser patte
    set_leg2(h_angle, 120)  # poser patte
    set_leg3(h_angle, 120)  # poser patte

# ================= MOUVEMENTS =================

def forward():
    global h_angle

    # cycle de marche simple
    lift()
    time.sleep(0.1)

    h_angle = 120
    set_leg0(h_angle, 60)
    set_leg1(h_angle, 60)
    set_leg2(h_angle, 60)
    set_leg3(h_angle, 60)
    time.sleep(0.1)

    down()
    time.sleep(0.1)

    h_angle = 60
    set_leg0(h_angle, 120)
    set_leg1(h_angle, 120)
    set_leg2(h_angle, 120)
    set_leg3(h_angle, 120)
    time.sleep(0.1)


def backward():
    global h_angle

    lift()
    time.sleep(0.1)

    h_angle = 60
    set_leg0(h_angle, 60)
    set_leg1(h_angle, 60)
    set_leg2(h_angle, 60)
    set_leg3(h_angle, 60)
    time.sleep(0.1)

    down()
    time.sleep(0.1)

    h_angle = 120
    set_leg0(h_angle, 120)
    set_leg1(h_angle, 120)
    set_leg2(h_angle, 120)
    set_leg3(h_angle, 120)
    time.sleep(0.1)


def turn_left():
    lift()
    time.sleep(0.1)

    set_leg0(60, 60)
    set_leg1(60, 60)
    set_leg2(60, 60)
    set_leg3(60, 60)
    time.sleep(0.2)

    down()


def turn_right():
    lift()
    time.sleep(0.1)

    set_leg0(120, 60)
    set_leg1(120, 60)
    set_leg2(120, 60)
    set_leg3(120, 60)
    time.sleep(0.2)

    down()


def attack():
    for _ in range(3):
        set_leg0(90, 50)
        set_leg1(90, 50)
        set_leg2(90, 50)
        set_leg3(90, 50)
        time.sleep(0.15)
        set_leg0(90, 130)
        set_leg1(90, 130)
        set_leg2(90, 130)
        set_leg3(90, 130)
        time.sleep(0.15)
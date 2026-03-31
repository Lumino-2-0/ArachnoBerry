import time
from machine import I2C, Pin
from grove_16_channels_pwm import Grove16PWM

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=100_000)
pwm = Grove16PWM(i2c)

# Angle global
angle = 90

# Initialisation
pwm.servo_angle(0, angle)
pwm.servo_angle(1, angle)

def forward():
    global angle
    angle += 5  # incrément

    if angle > 180:
        angle = 180

    pwm.servo_angle(0, angle)
    pwm.servo_angle(1, angle)

def backward():
    global angle
    angle -= 5  # décrément

    if angle < 0:
        angle = 0

    pwm.servo_angle(0, angle)
    pwm.servo_angle(1, angle)

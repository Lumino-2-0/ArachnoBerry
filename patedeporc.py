import time
from machine import I2C, Pin
from grove_16_channels_pwm import Grove16PWM

# Exemple avec I2C(0) et pins GP8/GP9
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=100_000)

# Création du pilote PCA9685
pwm = Grove16PWM(i2c)  # adresse par défaut = 0x7F, fréquence = 50 Hz

# Servomoteur 1 = channel 0
pwm.servo_angle(0, 90)

print("init patédeporc_lib = OK")

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
   

def forward():
    i = 0
    pwm.servo_angle(0,0+i)
    pwm.servo_angle(1,0+i)
    i = i+1
    
def backward():
    i = 0
    pwm.servo_angle(0,0+i)
    pwm.servo_angle(1,0+i)
    i = i-1
    
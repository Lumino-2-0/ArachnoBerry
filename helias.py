import time
from machine import I2C, Pin
from grove_16_channels_pwm import Grove16PWM

# ================= INIT =================

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=100_000)
pwm = Grove16PWM(i2c)

# ================= REGLAGES =================

Baisse = 45
Levee = 100

# Patte 2 et 3 ont un offset vertical spécial
Levee_Arriere = 0

Time_Pause = 0.2 # Valeur par défaut (200 ms)

Double = False

# ================= SERVOS =================

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

# ================= POSITION NEUTRE =================

def neutral():
    set_leg0(20, Baisse)
    set_leg1(80, Baisse)
    set_leg2(95, Baisse)
    set_leg3(40, Baisse)

# ================= AVANCER =================

def forward():

    if Double :
        set_leg0(20, Baisse) # La patte ce place vers l'avant tout en étant Baisse pour avoir le mouvement avec le frottement du sol
        set_leg2(95, Baisse) # La patte ce place vers l'avant tout en étant Baisse pour avoir le mouvement avec le frottement du sol
        time.sleep(Time_Pause)
        set_leg0(65, Baisse) # La patte ce place vers l'arrière (fin du mouvement de frottement)
        set_leg2(52, Baisse) # La patte ce place vers l'arrière (fin du mouvement de frottement)
        time.sleep(Time_Pause)
        set_leg0(65, Levee) # On relève la patte pour la remmettre en position de départ
        set_leg2(52, 0) # On relève la patte pour la remmettre en position de départ (0 car l'axe vertical de la patte 2 est pas bien positionné)
        time.sleep(Time_Pause)
        set_leg0(20, Levee) # On remet la patte en position de départ horizontale pour le prochain mouvement
        set_leg2(95, 0) # On remet la patte en position de départ horizontale pour le prochain mouvement (0 car l'axe vertical de la patte 2 est pas bien positionné)
        time.sleep(Time_Pause)
        set_leg0(20, Baisse) # On remet la patte qui touche le sol pour le prochain mouvement
        set_leg2(95, Baisse) # On remet la patte qui touche le sol pour le prochain mouvement
        
                
        set_leg1(95, Baisse)
        set_leg3(25, Baisse)
        time.sleep(Time_Pause)
        set_leg1(120, Baisse) # La patte ce place vers l'arrière (fin du mouvement de frottement)
        set_leg3(0, Baisse) # La patte ce place vers l'arrière (fin du mouvement de frottement)
        time.sleep(Time_Pause)
        set_leg1(120, Levee) # On relève la patte pour la remmettre en position de départ
        set_leg3(0, 0) # On relève la patte pour la remmettre en position de départ (0 car l'axe vertical de la patte 3 est pas bien positionné)
        time.sleep(Time_Pause)
        set_leg1(95, Levee) # On remet la patte en position de départ horizontale pour le prochain mouvement
        set_leg3(25, 0) # On remet la patte en position de départ horizontale pour le prochain mouvement (0 car l'axe vertical de la patte 3 est pas bien positionné)
        time.sleep(Time_Pause)
        set_leg1(95, Baisse) # On remet la patte qui touche le sol pour le prochain mouvement
        set_leg3(25, Baisse) # On remet la patte qui touche le sol pour le prochain mouvement

        
    
    else :
        set_leg0(20, Baisse) # La patte ce place vers l'avant tout en étant Baisse pour avoir le mouvement avec le frottement du sol
        time.sleep(Time_Pause)
        set_leg0(65, Baisse) # La patte ce place vers l'arrière (fin du mouvement de frottement)
        time.sleep(Time_Pause)
        set_leg0(65, Levee) # On relève la patte pour la remmettre en position de départ
        time.sleep(Time_Pause)
        set_leg0(20, Levee) # On remet la patte en position de départ horizontale pour le prochain mouvement
        time.sleep(Time_Pause)
        set_leg0(20, Baisse) # On remet la patte qui touche le sol pour le prochain mouvement

        set_leg2(95, Baisse) # La patte ce place vers l'avant tout en étant Baisse pour avoir le mouvement avec le frottement du sol
        time.sleep(Time_Pause)
        set_leg2(52, Baisse) # La patte ce place vers l'arrière (fin du mouvement de frottement)
        time.sleep(Time_Pause)
        set_leg2(52, 0) # On relève la patte pour la remmettre en position de départ (0 car l'axe vertical de la patte 2 est pas bien positionné)
        time.sleep(Time_Pause)
        set_leg2(95, 0) # On remet la patte en position de départ horizontale pour le prochain mouvement (0 car l'axe vertical de la patte 2 est pas bien positionné)
        time.sleep(Time_Pause)
        set_leg2(95, Baisse) # On remet la patte qui touche le sol pour le prochain mouvement


        set_leg1(95, Baisse)
        time.sleep(Time_Pause)
        set_leg1(120, Baisse) # La patte ce place vers l'arrière (fin du mouvement de frottement)
        time.sleep(Time_Pause)
        set_leg1(120, Levee) # On relève la patte pour la remmettre en position de départ
        time.sleep(Time_Pause)
        set_leg1(95, Levee) # On remet la patte en position de départ horizontale pour le prochain mouvement
        time.sleep(Time_Pause)
        set_leg1(95, Baisse) # On remet la patte qui touche le sol pour le prochain mouvement


        set_leg3(25, Baisse)
        time.sleep(Time_Pause)
        set_leg3(0, Baisse) # La patte ce place vers l'arrière (fin du mouvement de frottement)
        time.sleep(Time_Pause)
        set_leg3(0, 0) # On relève la patte pour la remmettre en position de départ (0 car l'axe vertical de la patte 3 est pas bien positionné)
        time.sleep(Time_Pause)
        set_leg3(25, 0) # On remet la patte en position de départ horizontale pour le prochain mouvement (0 car l'axe vertical de la patte 3 est pas bien positionné)
        time.sleep(Time_Pause)
        set_leg3(25, Baisse) # On remet la patte qui touche le sol pour le prochain mouvement

# ================= RECULER =================

def backward():
    # Même mouvement mais inversé
    
    if Double :
        set_leg0(65, Baisse)
        set_leg2(52, Baisse)
        time.sleep(Time_Pause)

        set_leg0(20, Baisse)
        set_leg2(95, Baisse)
        time.sleep(Time_Pause)
        
        set_leg0(20, Levee)
        set_leg2(95, Levee_Arriere)
        time.sleep(Time_Pause)
        
        set_leg0(65, Levee)
        set_leg2(52, Levee_Arriere)
        time.sleep(Time_Pause)
        
        set_leg0(65, Baisse)
        set_leg2(52, Baisse)
        time.sleep(Time_Pause)

        set_leg1(110, Baisse)
        set_leg3(10, Baisse)
        time.sleep(Time_Pause)

        set_leg1(80, Baisse)
        set_leg3(40, Baisse)
        time.sleep(Time_Pause)

        set_leg1(80, Levee)
        set_leg3(40, Levee_Arriere)
        time.sleep(Time_Pause)
        
        set_leg1(110, Levee)
        set_leg3(10, Levee_Arriere)
        time.sleep(Time_Pause)
        
        set_leg1(110, Baisse)
        set_leg3(10, Baisse)
        
    else :
        set_leg0(65, Baisse)
        time.sleep(Time_Pause)
        set_leg0(20, Baisse)
        time.sleep(Time_Pause)
        set_leg0(20, Levee)
        time.sleep(Time_Pause)
        set_leg0(65, Levee)
        time.sleep(Time_Pause)
        set_leg0(65, Baisse)
        time.sleep(Time_Pause)

        set_leg2(52, Baisse)
        time.sleep(Time_Pause)
        set_leg2(95, Baisse)
        time.sleep(Time_Pause)
        set_leg2(95, Levee_Arriere)
        time.sleep(Time_Pause)
        set_leg2(52, Levee_Arriere)
        time.sleep(Time_Pause)
        set_leg2(52, Baisse)
        
        set_leg1(110, Baisse)
        time.sleep(Time_Pause)
        set_leg1(80, Baisse)
        time.sleep(Time_Pause)
        set_leg1(80, Levee)
        time.sleep(Time_Pause)
        set_leg1(110, Levee)
        time.sleep(Time_Pause)
        set_leg1(110, Baisse)
        
        set_leg3(10, Baisse)
        time.sleep(Time_Pause)
        set_leg3(40, Baisse)
        time.sleep(Time_Pause)
        set_leg3(40, Levee_Arriere)
        time.sleep(Time_Pause)
        set_leg3(10, Levee_Arriere)
        time.sleep(Time_Pause)
        set_leg3(10, Baisse)

# ================= TOURNER =================

def turn_left():

    # côté gauche recule
    set_leg0(65, Baisse)
    time.sleep(Time_Pause)

    set_leg0(20, Baisse)
    time.sleep(Time_Pause)

    set_leg0(20, Levee)
    time.sleep(Time_Pause)

    set_leg0(65, Levee)
    time.sleep(Time_Pause)

    set_leg0(65, Baisse)

    # côté droit avance
    set_leg1(95, Baisse)
    time.sleep(Time_Pause)

    set_leg1(120, Baisse)
    time.sleep(Time_Pause)

    set_leg1(120, Levee)
    time.sleep(Time_Pause)

    set_leg1(95, Levee)
    time.sleep(Time_Pause)

    set_leg1(95, Baisse)

    # arrière gauche recule
    set_leg2(52, Baisse)
    time.sleep(Time_Pause)

    set_leg2(95, Baisse)
    time.sleep(Time_Pause)

    set_leg2(95, Levee_Arriere)
    time.sleep(Time_Pause)

    set_leg2(52, Levee_Arriere)
    time.sleep(Time_Pause)

    set_leg2(52, Baisse)

    # arrière droit avance
    set_leg3(25, Baisse)
    time.sleep(Time_Pause)

    set_leg3(0, Baisse)
    time.sleep(Time_Pause)

    set_leg3(0, Levee_Arriere)
    time.sleep(Time_Pause)

    set_leg3(25, Levee_Arriere)
    time.sleep(Time_Pause)

    set_leg3(25, Baisse)
    
# ================= TOURNER =================

def turn_right():

    # côté gauche avance
    set_leg0(20, Baisse)
    time.sleep(Time_Pause)

    set_leg0(65, Baisse)
    time.sleep(Time_Pause)

    set_leg0(65, Levee)
    time.sleep(Time_Pause)

    set_leg0(20, Levee)
    time.sleep(Time_Pause)

    set_leg0(20, Baisse)

    # côté droit recule
    set_leg1(120, Baisse)
    time.sleep(Time_Pause)

    set_leg1(95, Baisse)
    time.sleep(Time_Pause)

    set_leg1(95, Levee)
    time.sleep(Time_Pause)

    set_leg1(120, Levee)
    time.sleep(Time_Pause)

    set_leg1(120, Baisse)

    # arrière gauche avance
    set_leg2(95, Baisse)
    time.sleep(Time_Pause)

    set_leg2(52, Baisse)
    time.sleep(Time_Pause)

    set_leg2(52, Levee_Arriere)
    time.sleep(Time_Pause)

    set_leg2(95, Levee_Arriere)
    time.sleep(Time_Pause)

    set_leg2(95, Baisse)

    # arrière droit recule
    set_leg3(0, Baisse)
    time.sleep(Time_Pause)

    set_leg3(25, Baisse)
    time.sleep(Time_Pause)

    set_leg3(25, Levee_Arriere)
    time.sleep(Time_Pause)

    set_leg3(0, Levee_Arriere)
    time.sleep(Time_Pause)

    set_leg3(0, Baisse)
    
# ================= ATTAQUE =================

def attack_left():

    #Lever une patte en avant et faire trembler à la vertical (L0 seumement)
    
    set_leg0(20, Baisse)
    time.sleep(Time_Pause)
    set_leg0(20, Levee)
    set_leg0(30, Levee)
    time.sleep(Time_Pause)
    set_leg0(20, Levee)
    set_leg0(30, Levee)
    time.sleep(Time_Pause)
    set_leg0(20, Baisse)
    
def attack_right(): #L2
    
    #Lever une patte en avant et faire trembler à la vertical (L2 seumement)
    
    set_leg2(95, Baisse)
    time.sleep(Time_Pause)
    set_leg2(95, Levee_Arriere)
    set_leg2(105, Levee_Arriere)
    time.sleep(Time_Pause)
    set_leg2(95, Levee_Arriere)
    set_leg2(105, Levee_Arriere)
    time.sleep(Time_Pause)
    set_leg2(95, Baisse)
     
    


# ================= TEST =================

def Servo_test():
    for i in range(20, 120, 5):
        set_leg0(i, Baisse)
        set_leg1(i+60, Baisse)
        set_leg2(i+75, Baisse)
        set_leg3(i+20, Baisse)
        time.sleep(0.1)


def Jump():

    time.sleep(0.5)

    set_leg0(20, Baisse)
    set_leg1(80, Baisse)
    set_leg2(95, Baisse)
    set_leg3(40, Baisse)
    
    time.sleep(0.25)
    
    set_leg0(20, Levee)
    set_leg1(80, Levee)
    set_leg2(95, Levee_Arriere)
    set_leg3(40, Levee_Arriere)
from microbit import *
from lib_maqueen import *



# test si le bus i2c est actif
while not power_is_on():
    pass

while True :

    # Ecriture sortie Led
    if capteurD() == 1 :
        allume_led('D')
    elif capteurG() == 1:
        allume_led('G')

    #eviteur
    if mesure_distance() < 5:
        moteurG(-50)
        moteurD(50)
        sleep(1500)

    #suivi ligne
    else :
        if capteurG() == 0 and capteurD() == 0 :
            moteurG(40)
            moteurD(45)
        elif capteurG() == 1 and capteurD() == 0 :
            moteurG(40)
            moteurD(10)
        elif capteurG() == 0 and capteurD() == 1 :
            moteurG(10)
            moteurD(40)
        else :
            moteurG(-40)
            moteurD(-40)
            sleep(500)
            moteurG(50)
            moteurD(-50)
            sleep(300)
            moteurG(40)
            moteurD(45)
            sleep(800)

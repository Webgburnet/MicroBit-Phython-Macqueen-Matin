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
    else :
        eteint_led('D')
        eteint_led('G')
    
    #eviteur
    if mesure_distance() < 5:
        moteurG(-50)
        moteurD(50)
        sleep(1500)
    else :
        moteurG(50)
        moteurD(50)
    
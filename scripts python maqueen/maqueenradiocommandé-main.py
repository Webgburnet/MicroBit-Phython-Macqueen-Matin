# Imports go at the top
from microbit import *
from lib_maqueen import *
import radio

radio.config(group = 5)
radio.on()
# test si le bus i2c est actif
while not power_is_on():
    pass
# Code in a 'while True:' loop repeats forever
while True :
   

   
        if radio.receive() == 'avance':
            display.show(Image.ARROW_N)
            moteurG(40)
            moteurD(40)
            sleep(100)
            display.clear()
        elif radio.receive() == "recule":
            display.show(Image.ARROW_S)
            moteurG(-40)
            moteurD(-40)
        elif radio.receive() == "gauche":
            display.show(Image.ARROW_W)
            moteurG(10)
            moteurD(40)
        elif radio.receive() == "droite":
            display.show(Image.ARROW_E)
            moteurG(40)
            moteurD(10)
        elif radio.receive() == "demi":
            display.show(Image.ANGRY)
            moteurG(40)
            moteurD(-40)
            sleep(1500)
        elif radio.receive() == "stop":
            display.show(Image.NO)
            moteurG(0)
            moteurD(0)


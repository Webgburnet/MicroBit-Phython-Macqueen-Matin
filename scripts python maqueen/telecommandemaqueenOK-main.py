# Imports go at the top
from microbit import *
import radio

#def envoyer(message) :
   # radio.send(message)


radio.config(group = 5)
radio.on()
# Code in a 'while True:' loop repeats forever
while True :
    display.clear()
    if accelerometer.is_gesture('down'):
        display.show(Image.ARROW_N)
        radio.send('avance')
    elif accelerometer.is_gesture('up'):
        display.show(Image.ARROW_S)
        radio.send("recule")
    elif accelerometer.is_gesture('left'):
        display.show(Image.ARROW_W)
        radio.send("gauche")
    elif accelerometer.is_gesture('right'):
        display.show(Image.ARROW_E)
        radio.send("droite")
    elif button_a.is_pressed() :
        radio.send("demi")
        display.show(Image.ANGRY)
    elif button_b.is_pressed() :
        radio.send("stop")
        display.show(Image.NO)




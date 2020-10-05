from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

r = randint(0,255)
g = randint(0,255)
b = randint(0,255)

x = 0
y = 0

sense.set_pixel(x,y,r,g,b)
sleep(0.25)

x = 7
y = 7

sense.set_pixel(x,y,r,g,b)
sleep(0.25)

x = 7
y = 0

sense.set_pixel(x,y,r,g,b)
sleep(0.25)

x = 0
y = 7

sense.set_pixel(x,y,r,g,b)
sleep(0.25)
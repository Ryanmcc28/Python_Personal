import pyautogui as pag
import time
import random
import math

num = 5
while 5:
    num += 1
    x = random.randint(600,700)
    y = random.randint(200,600)
    pag.moveTo(x,y,0.1)

    time.sleep(3)
    
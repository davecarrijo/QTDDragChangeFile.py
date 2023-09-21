import time
import pyautogui as pg

screenWidth, screenHeight = pg.size()

pg.moveTo(750, 300)
pg.click()
#rotate 90'n degress
def Rotate90D():
    pg.rightClick()
    pg.move(20, 5)
    pg.rightClick()

for i in range(2):
    Rotate90D()

# FLip the canvas horizontal
def flipHorizontal():
    pg.rightClick()
    pg.move(40,75)
    pg.rightClick()

flipHorizontal()
pg.moveTo(100, 700)

# Stationary mouse mode
for i in range(2):
    pg.click
from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

#Button and dinosaur coordinates (You may have other coordinates depending on your screen resolution)
class Cordinates():
    restGame = (336, 314)
    dino = (104, 323)
    

#Pressing the restart button
def restartGame():
    pyautogui.click(Cordinates.restGame)

#Jump
def pressSpace():
    pyautogui.keyDown ('space')
    time.sleep(0.05)
    print("Jump") 
    pyautogui.keyUp ('space')

#grab
def imageGrab():
    box = (Cordinates.dino[0]+62, Cordinates.dino[1], Cordinates.dino[0]+102, Cordinates.dino[1]+33)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()

def main():
    restartGame()
    while True:
        if imageGrab() != 1575:
            pressSpace()
            time.sleep(0.01)         

main()

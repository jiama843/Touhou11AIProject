#import os
import pyautogui
#from pynput.keyboard import Key, Controller
from ScreenReader import ScreenReader
from NNData import NNDatabase
import ImageGrab
import time

#keyboard = Controller()

def findOutput(outputArr):
    maxOutput = outputArr[0]
    for i in range(0, len(outputArr)):
        if(outputArr[i].val > maxOutput.val):
            maxOutput = outputArr[i]
    print(maxOutput.keyID)
    return maxOutput

def runGame():

    image = ImageGrab.grab()
    color = image.getpixel((70, 370))

    pyautogui.keyDown('z')

    #for i in range(0, 1):
    while(color != (64, 8, 8) and image.getpixel((70, 400)) != (64, 8, 8)):

        image = ImageGrab.grab()
        color = image.getpixel((70, 370))

        print(color)
        #time.sleep(0.2)
        #pyautogui.moveTo(70, 370)
        #os.system('python ScreenReader.py')
        sr = ScreenReader.ScreenReader()

        inputArr = sr.getInputArr()

        #print(len(inputArr))
        #print(len(inputArr[1]))
        #print(inputArr[0][0])

        """for i in range(0, len(inputArr)):
            for j in range(0, len(inputArr[i])):
                print(inputArr[i][j], end=",")
            print("")"""
        """
        print(len(NNDatabase.population))"""
        outputArr = NNDatabase.population[0].evaluate(inputArr)
        output = findOutput(outputArr)
        #keyboard.press(Key.right)
        #keyboard.release(Key.right)
        pyautogui.keyDown(output.keyID)
        pyautogui.keyUp(output.keyID)

    pyautogui.keyUp('z')

    #return fitness

    """for i in range(0, len(outputArr)):
        outputArr[i].printNodeGene()
        print(outputArr[i].val)"""

def runController():

    #will evaluate fitness in runGame() and return it
    runGame()
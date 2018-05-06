import pyautogui
#from colorama import Fore, Back, Style
#from termcolor import colored
import ImageGrab
import time

class ScreenReader:

    def getInputArr(self):
        #pyautogui.moveTo(420, 490)
        #pyautogui.moveTo(30, 30)
        #time.sleep(1.0)
        #time.clock()

        inputArr = [[]]

        image = ImageGrab.grab()
        #time.sleep(1.0)
        #resolution of game screen is ~ 400x400
        #store normalized inputs in a numpy array and feed it into the neural network
        #store screen pixels in an array named "prev pixels" and then check if every pixel is a duplicate. This means the character has died
        #   Set the time that previous pixels are checked to the time that fitness starts=
        for x in range(30, 420, 5):
            linputArr = []
            for y in range(30, 490, 5):
                color = image.getpixel((x, y))
                if(color == (0, 0, 0)):#color == (35, 171, 35) or color == (1, 1, 1) or color == (1, 103, 1)):
                    # BG
                    linputArr.append(0)
                    #print("BG")
                elif(color == (255, 34, 221) or color == (255, 51, 221)):
                    # Character
                    linputArr.append(-1)
                    #print("character")
                else:
                    # Obstacle
                    linputArr.append(1)
                    #print("Obstacle")
                """print("x = ")
                print((x - 30)/10)
                print("y = ")
                print((y - 30)/10)"""
            inputArr.append(linputArr)
        print(time.clock())

        return inputArr
        #must return a list of lists of screen pixels


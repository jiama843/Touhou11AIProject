#import os
import pyautogui
import random
#from pynput.keyboard import Key, Controller
from ScreenReader import ScreenReader
from NNData import NNDatabase
from NEATAlgorithm import THNetwork
from NEATAlgorithm import GeneratePopulation
import ImageGrab
import time

#keyboard = Controller()
"""def numExcess(network1, network2):

    # Iterate through Conns

def numDisjoint(network1, network2):

    #

def avgWeightDiff(network1, network2):"""

# findMDE takes in minConns, maxConns and a boolean that determines
# whether or not the function should determine matchingConns or
# weight difference , and will create a new triplet that contains lists for:
# matchingConns/weightDiff, disjointConns and excessConns
def findMDE(minConns, maxConns):

    connDict = {}

    excess = []
    disjoint = []
    matching = []

    avgWeightDiff = 0

    maxID = 0
    for i in range(0, len(minConns)):
        if(minConns[i].innovationID > maxID):
            maxID = minConns[i].innovationID

        connDict[minConns[i].innovationID] = minConns[i]

    for i in range(0, len(maxConns)):

        if maxConns[i].innovationID in connDict:

            inheritVar = random.randint(0,1)

            if(inheritVar == 0):
                matching.append(maxConns[i])
            else:
                matching.append(connDict[maxConns[i].innovationID])

            avgWeightDiff += abs(maxConns[i].weight - connDict[maxConns[i].innovationID].weight)

        else:
            if(maxConns[i].innovationID > maxID):
                excess.append(maxConns[i])
            else:
                disjoint.append(maxConns[i])

    avgWeightDiff /= len(matching)

    dictMDE = {}
    dictMDE['avgWeightDiff'] = avgWeightDiff
    dictMDE['matching'] = matching
    dictMDE['disjoint'] = disjoint
    dictMDE['excess'] = excess

    return dictMDE


def crossover(network1, network2):

    maxNetwork: THNetwork
    minNetwork: THNetwork
    if(network1.numConns > network2.numConns):
        maxNetwork = network1
        minNetwork = network2
    else:
        maxNetwork = network2
        minNetwork = network1

    MDE = findMDE(minNetwork.connGenes, maxNetwork.connGenes)

    newSpeciationID = getSpeciationID(list(MDE['matching']) + list(MDE['disjoint']) + list(MDE['excess']))

    newNetwork: THNetwork

    #if there is a new species, we need to append a new list of networks in NNDatabase.population
    if(newSpeciationID >= len(NNDatabase.population) - 1):
        newSpecies = []
        newNetwork = THNetwork.THNetwork(newSpeciationID, 0)
        newSpecies.append(newNetwork)
        NNDatabase.population.append(newSpecies)
    else:
        newNetwork = THNetwork.THNetwork(newSpeciationID, len(NNDatabase.population[newSpeciationID]))
        NNDatabase.population[newSpeciationID].append(newNetwork)

    newNetwork.setNodeGenes(list(maxNetwork.nodeGenes))
    newNetwork.setConnGenes(list(MDE['matching']) + list(MDE['disjoint']) + list(MDE['excess']))


# getSpeciationID accepts a list of connGenes and will determine respective speciationID
def getSpeciationID(connGenes):

    compThreshold = 3.0

    c1 = 1
    c2 = 1
    c3 = 0.2

    print(len(NNDatabase.population))
    for i in range(0, len(NNDatabase.population)):

        print(len(NNDatabase.population[i]) - 1)
        ranIndex = random.randint(0, len(NNDatabase.population[i]) - 1)

        maxConns: []
        minConns: []
        if (len(connGenes) > NNDatabase.population[i][ranIndex].numConns):
            maxConns = NNDatabase.population[i][ranIndex].connGenes
            minConns = connGenes
        else:
            maxConns = connGenes
            minConns = NNDatabase.population[i][ranIndex].connGenes

        MDE = findMDE(minConns, maxConns)

        N = len(maxConns)

        comp = (c1 * len(MDE['disjoint'])/N) + (c2 * len(MDE['excess'])/N) + (c3 * MDE['avgWeightDiff'])

        print(comp)

        if(comp <= compThreshold):
            return i

    return len(NNDatabase.population)


def resetGame():
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    time.sleep(0.5)
    pyautogui.keyUp('enter')
    time.sleep(0.5)
    pyautogui.keyDown('enter')
    time.sleep(0.5)
    pyautogui.keyUp('enter')
    time.sleep(0.5)
    pyautogui.keyDown('enter')
    time.sleep(0.5)
    pyautogui.keyUp('enter')
    time.sleep(0.5)
    pyautogui.keyDown('enter')
    time.sleep(0.5)
    pyautogui.keyUp('enter')
    time.sleep(0.5)



def findOutput(outputArr):
    maxOutput = outputArr[0]
    for i in range(0, len(outputArr)):
        if(outputArr[i].val > maxOutput.val):
            maxOutput = outputArr[i]
    print(maxOutput.keyID)
    return maxOutput

# rungame takes a speciesID and a genomeID and runs evaluate on the appropriate network with given screen
def runGame(speciationID, genomeID):

    #initiate game with enter
    pyautogui.keyDown('enter')
    time.sleep(0.4)
    pyautogui.keyUp('enter')
    time.sleep(0.4)

    fitness = 0

    image = ImageGrab.grab()
    color = image.getpixel((70, 370))

    pyautogui.keyDown('z')

    #for i in range(0, 1):
    while(color != (64, 8, 8) and image.getpixel((70, 400)) != (64, 8, 8) and image.getpixel((74, 252)) != (238, 136, 136)):
        fitness += 1

        image = ImageGrab.grab()
        color = image.getpixel((70, 370))

        print(color)
        print(fitness)
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
        outputArr = NNDatabase.population[speciationID][genomeID].evaluate(inputArr)
        output = findOutput(outputArr)
        #keyboard.press(Key.right)
        #keyboard.release(Key.right)
        if(output.keyID == "idle"): continue
        pyautogui.keyDown(output.keyID)
        pyautogui.keyUp(output.keyID)

    pyautogui.keyUp('z')

    time.sleep(0.2)

    # reset game
    resetGame()

    time.sleep(0.2)

    return fitness

    """for i in range(0, len(outputArr)):
        outputArr[i].printNodeGene()
        print(outputArr[i].val)"""

def runController():

    #will evaluate fitness in runGame() and return it
    #Change it to iterate through all NNDatabase population networks

    GeneratePopulation.generateNodes(78, 92)
    NNDatabase.population = GeneratePopulation.generatePopulation(10) #GeneratePopulation returns "pop", so we need to manually store it

    print(len(NNDatabase.population))

    for i in range(0, 10):

        for species in range(0, len(NNDatabase.population)):
            for genome in range(0, len(NNDatabase.population[species])):
                NNDatabase.population[species][genome].mutateAddNode()
                NNDatabase.population[species][genome].mutateAddConn()


                if(NNDatabase.population[species][genome].fitness == 0):
                    fitness = runGame(species, genome)  # Now, we run evaluate fitness for species: species and genome: genome

                NNDatabase.population[species][genome].fitness = fitness

                if (NNDatabase.maxFitness < fitness): NNDatabase.maxFitness = fitness
                print(fitness)

        #fitness = runGame(0, 0)  # Now, we run evaluate fitness for species: 0 and genome: 0

    print(NNDatabase.maxFitness)
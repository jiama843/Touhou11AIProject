import numpy
#import NEATAlgorithm THGene should already be available
from NNData import NNDatabase
from NEATAlgorithm import THGene
import random

"""This class represents the template of the network
A population of networks will be represented as a list of this class"""

class THNetwork:
    speciationID: int
    genomeID: int
    numConns = 0
    numNodes = 0

    nodeGenes: []
    connGenes: []  # This is a list of THConnGenes
                # consider converting to numpy array

    fitness: int

    def __init__(self, speciationID, genomeID):
        self.speciationID = speciationID
        self.genomeID = genomeID
        self.nodeGenes = []
        self.connGenes = []
        self.fitness = -1

    def printTHNetwork(self):
        print("Species: " + str(self.speciationID) + " Genome: " + str(self.genomeID))

        for i in range(0, len(self.connGenes)):
            self.connGenes[i].printConnGene()

        print("\n")
        #print node and conn in loop
        #print("This is a test.")

    def addNodeGene(self, ng):
        ng.localID = self.numNodes
        self.numNodes += 1
        self.nodeGenes.append(ng)

    def addConnGene(self, cg):

        #modify nodeGenes
        #cg.input

        self.numConns += 1
        self.connGenes.append(cg)

    def setNodeGenes(self, ngs):
        self.numNodes = len(ngs)
        self.nodeGenes = ngs

    def setConnGenes(self, cgs):
        self.numConns = len(cgs)
        self.connGenes = cgs

    def setFitness(self, f):
        self.fitness = f

    def containsNode(self, node):
        for i in range(self.numNodes):
            if(node == self.nodeGenes[i]):
                return True

        return False

    def containsConn(self, conn):
        for i in range(self.numConns):
            if(conn.innovationID == self.connGenes[i].innovationID):
                return True

        return False

    def mutateAddNode(self):
        newNode = THGene.THNodeGene(0, "Hidden", False, False)

        connIndex = random.randint(0, self.numConns - 1)
        existingConn = self.connGenes[connIndex]
        self.connGenes[connIndex].disable() #disable existing conn

        # add new incoming nodes
        newNode.incoming.append(self.connGenes[connIndex].input)
        self.connGenes[connIndex].output.incoming.append(newNode)
        self.addNodeGene(newNode) #append the newNodeGene

        # create 2 new ConnGenes
        newInputConn = THGene.THConnGene(existingConn.input, newNode, existingConn.weight, True)
        newOutputConn = THGene.THConnGene(newNode, existingConn.output, 1, True)

        self.addConnGene(newInputConn)
        self.addConnGene(newOutputConn)

    def mutateAddConn(self):
        validINodes = []
        validONodes = []

        for i in range(0, self.numNodes):

            if(self.nodeGenes[i].isInput == True or
                    (self.nodeGenes[i].isInput == False and self.nodeGenes[i].isOutput == False)):
                validINodes.append(self.nodeGenes[i])

            if(self.nodeGenes[i].isOutput == True or
                    (self.nodeGenes[i].isInput == False and self.nodeGenes[i].isOutput == False)):
                validONodes.append(self.nodeGenes[i])

        iIndex = random.randint(0, len(validINodes) - 1)
        oIndex = random.randint(0, len(validONodes) - 1)

        if(validONodes[oIndex].localID == validINodes[iIndex].localID and oIndex != len(validONodes) - 1): oIndex += 1
        elif(validONodes[oIndex].localID == validINodes[iIndex].localID and oIndex != 0): oIndex -= 1


        newConn = THGene.THConnGene(validINodes[iIndex], validONodes[oIndex], 1, True)
        validONodes[oIndex].incoming.append(validINodes[iIndex])
        if(self.containsConn(newConn) == False): self.addConnGene(newConn)

    def evaluate(self, inputArr):

        tempNodes = list(self.nodeGenes)
        tempConns = list(self.connGenes)

        for i in range(0, len(tempNodes)):
            if(tempNodes[i].IsInput() == True):
                tempNodes[i].val = inputArr[tempNodes[i].screenPosX][tempNodes[i].screenPosY] #sets the value of tempNodes to
                                                                                            # the normalized value of inputArr
                tempNodes[i].hasVal = True; #Don't have to worry about setting to false since tempNodes is a copy

        i = 0
        while i < len(tempNodes):

            if(tempNodes[i].isInput): i += 1; continue

            canEvaluate = True #if the incoming array is not empty, you can evaluate

            for j in range(0, len(tempNodes[i].incoming)):
                if(tempNodes[i].incoming[j].hasVal == False):
                    canEvaluate = False

            if(canEvaluate):
                tempNodes[i].val = 0

                # add all inputs, then apply activation function at the end
                for j in range(0, len(tempConns)):
                    if(tempConns[j].isEnabled and tempNodes[i].localID == tempConns[j].output.localID):
                        tempNodes[i].val = tempNodes[i].val + (tempConns[j].input.val * tempConns[j].weight)

                tempNodes[i].hasVal = True

            else:

                tempNodes.append(tempNodes[i])
                tempNodes.pop(i)
                i -= 1

            i += 1

        outputs = []
        for i in range(0, len(tempNodes)):
            if(tempNodes[i].isOutput and tempNodes[i].hasVal):
                outputs.append(tempNodes[i])

        return outputs


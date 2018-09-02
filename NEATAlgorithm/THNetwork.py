import numpy
#import NEATAlgorithm THGene should already be available
from NNData import NNDatabase
from NEATAlgorithm import THGene
import random
import copy

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

    fitness = 0

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
        self.nodeGenes[cg.output.localID].incoming.append(cg.input)

    def setNodeGenes(self, ngs):
        self.numNodes = len(ngs)
        self.nodeGenes = ngs

    def setConnGenes(self, cgs):
        self.numConns = len(cgs)
        self.connGenes = cgs

        for i in range(0, self.numConns):
            # print(testNetwork.connGenes[i].isEnabled)
            if (self.connGenes[i].isEnabled):
                self.nodeGenes[self.connGenes[i].output.localID].incoming.append(self.connGenes[i].input)

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

    """def mutateAddInput(self):

        inputX = random.randint(0, 83)
        inputY = random.randint(0, 97)

        newNode = NNDatabase.population[inputX, inputY]

        if(self.containsNode(newNode) == False):
            self.addNodeGene(newNode)"""

    def mutateAddNode(self):
        newNode = THGene.THNodeGene(0, "Hidden", False, False)

        connIndex = random.randint(0, self.numConns - 1)
        existingConn = self.connGenes[connIndex]
        self.connGenes[connIndex].disable() #disable existing conn

        # add new incoming nodes
        #newNode.incoming.append(self.connGenes[connIndex].input)
        #self.connGenes[connIndex].output.incoming.append(newNode)
        self.addNodeGene(newNode) #append the newNodeGene

        print("MUTATE LOCALID BELOW")
        print(newNode.localID)

        # create 2 new ConnGenes
        newInputConn = THGene.THConnGene(existingConn.input, newNode, existingConn.weight, True)
        newOutputConn = THGene.THConnGene(newNode, existingConn.output, 1, True)

        self.addConnGene(newInputConn)
        self.addConnGene(newOutputConn)

        self.fitness = 0

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
        #validONodes[oIndex].incoming.append(validINodes[iIndex])
        if(self.containsConn(newConn) == False): self.addConnGene(newConn)

        self.fitness = 0

    def evaluate(self, inputArr):

        tempNodes = copy.deepcopy(self.nodeGenes)
        tempConns = copy.deepcopy(self.connGenes)

        print(len(tempNodes))
        print(len(self.nodeGenes))
        print(len(tempConns))

        #set incoming for tempNodeGenes
        for i in range(0, len(tempNodes)):
            for j in range(0, len(tempNodes[i].incoming)):
                #print(i)
                #print(j)
                #print(tempNodes[i].incoming[j].localID)
                tempNodes[i].incoming[j] = tempNodes[tempNodes[i].incoming[j].localID]

        #print(len(NNDatabase.inputs))
        #print(len(NNDatabase.inputs[0]))

        #print(len(inputArr))
        #print(len(inputArr[0]))


        for i in range(0, len(tempNodes)):
            if(tempNodes[i].IsInput() == True):
                tempNodes[i].val = inputArr[tempNodes[i].screenPosX][tempNodes[i].screenPosY] #sets the value of tempNodes to
                                                                                            # the normalized value of inputArr
                tempNodes[i].hasVal = True #Don't have to worry about setting to false since tempNodes is a copy

        i = 0
        while i < len(tempNodes):
            #print("infinite recursion")
            print("CURR TEMPNODE AND ITS LOCAL ID:")
            print(i)
            print(tempNodes[i].localID)
            #print(len(tempNodes))
            if(tempNodes[i].isInput): i += 1; continue

            canEvaluate = True #if the incoming array is not empty, you can evaluate

            for j in range(0, len(tempNodes[i].incoming)):
                if(tempNodes[i].incoming[j].hasVal == False):
                    print("FAILS ON THE NODE BELOW (WITH LOCAL ID)")
                    print(tempNodes[i].incoming[j].localID)
                    canEvaluate = False
                    break

            if(canEvaluate):
                tempNodes[i].val = 0

                # add all inputs, then apply activation function at the end
                for j in range(0, len(tempConns)):
                    if(tempConns[j].isEnabled and tempNodes[i].localID == tempConns[j].output.localID):

                        tempNodes[i].value = tempNodes[i].value + (tempConns[j].input.value * tempConns[j].weight)

                ##
                ###

                #
                #
                #
                #

                #
                #
                #
                #
                ##IS THE LINE BELOW UPDATING THE INCOMING NODES???????!!!!!!!!!
                print("TEMP NODE UPDATE BELOW")
                print(tempNodes[i].localID)
                print("I at the time:")
                print(i)
                tempNodes[i].hasVal = True

            else:


                #IS THE BELOW CODE GENERATING A COPY?
                #APPARENTLY ITS GENERATING A REFERENCE SO EVERYTHING IS FINE
                tempNodes.append(tempNodes[i])
                tempNodes.pop(i)
                i -= 1

            i += 1

        outputs = []
        for i in range(0, len(tempNodes)):
            if(tempNodes[i].isOutput and tempNodes[i].hasVal):
                outputs.append(tempNodes[i])

        return outputs


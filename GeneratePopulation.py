import numpy
import tensorflow
from NEATAlgorithm import THNetwork #What is this beautiful stuff?
from NEATAlgorithm import THGene
from NNData import NNDatabase
import random

#count should be sqrt(1521) = 39
def generateNodes(width, length):
    #nodes = []

    right = THGene.THNodeGene(0, "right", False, True)
    #nodes.append(right)
    NNDatabase.outputs.append(right)

    left = THGene.THNodeGene(1, "left", False, True)
    #nodes.append(left)
    NNDatabase.outputs.append(left)

    up = THGene.THNodeGene(2, "up", False, True)
    #nodes.append(up)
    NNDatabase.outputs.append(up)

    down = THGene.THNodeGene(3, "down", False, True)
    #nodes.append(down)
    NNDatabase.outputs.append(down)

    # from [1][0] to [84][98]
    for i in range(0, width):
        lNodes = []
        for j in range(0, length):
            newGene = THGene.THNodeGene(i, "input", True, False)
            newGene.screenPosX = i
            newGene.screenPosY = j
            lNodes.append(newGene)
            #nodes.append(newGene)
        #print(len(lNodes))
        NNDatabase.inputs.append(lNodes)

    #print(len(NNDatabase.inputs))
    #print(NNDatabase.inputs[1][0])
    #print(NNDatabase.inputs[84][97])
    #return nodes

def generateConns(count):
    conns = []

#""" Create a global variable to store innovationID and nodes before any further progress can be made on this"""
    for i in range(0, count):
        node1 = random.randint(0, NNDatabase.numNodeGenes)
        node2 = random.randint(0, NNDatabase.numNodeGenes)

        if node1 > node2 or node1 == node2:
            i -= 1
            continue

        newConn = THGene.THConnGene(NNDatabase.nodeGenes[node1], NNDatabase.nodeGenes[node2], 1, True)
        #NNDatabase.innovationID += 1
        conns.append(newConn)


def generatePopulation(count):
    """Count is the number of networks to generate preferably about 20"""

    "Declare population as an array"
    pop = []

    for i in range(0, count):
        numInputs = random.randint(1, 10) #anywhere from 1 to 10 input nodes
        numConns = random.randint(1, numInputs + 3)
        newNetwork = THNetwork.THNetwork(i, 0)

        for j in range(0, numInputs):
            inputX = random.randint(1, 84)
            inputY = random.randint(0, 97)

            #local scope newNode
            newNode = NNDatabase.inputs[inputX][inputY]
            newNode.localID = j

            if(newNetwork.containsNode(newNode) == False):
                newNetwork.addNodeGene(newNode)

            j -= 1

        for outID in range(0, 4):

            #local scope newNode
            newNode = NNDatabase.outputs[outID]
            newNode.localID = numInputs + outID

            newNetwork.addNodeGene(newNode)

        # for each Network, we need to create/append ConnGenes etc...
        for j in range(0, numConns):
            inputID = random.randint(0, numInputs - 1)

            # we need to check compatibility distance and adjust innovationID accordingly
            outputID = random.randint(numInputs, numInputs + 3) # r u kidding me, it was 0 - 3 not 0 - 4

            #print(inputID)
            #print(outputID)

            newConn = THGene.THConnGene(newNetwork.nodeGenes[inputID], newNetwork.nodeGenes[outputID], 1, True)

            #I think we should randomly generate nodeGenes first, then while randomly generating connGenes, we modify local nodeGenes
            #newNetwork.addNodeGene(NNDatabase.inputs[inputX][inputY])
            #newNetwork.addNodeGene(NNDatabase.outputs[outputID])
            if(newNetwork.containsConn(newConn) == False):
                newNetwork.addConnGene(newConn)

            # NNDatabase.innovationID += 1

        pop.append(newNetwork)

    return pop


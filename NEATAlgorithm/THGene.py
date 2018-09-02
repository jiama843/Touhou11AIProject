import numpy
from NNData import NNDatabase

def findInnovation(input, output):
    for i in range(0, len(NNDatabase.connGenes)):
        if(NNDatabase.connGenes[i].input.localID == input.localID and
                NNDatabase.connGenes[i].output.localID == output.localID):
            return NNDatabase.connGenes[i].innovationID

    NNDatabase.innovationID += 1
    return NNDatabase.innovationID

def connExists(input, output):
    for i in range(0, len(NNDatabase.connGenes)):
        if(NNDatabase.connGenes[i].input == input and NNDatabase.connGenes[i].output == output):
            return True

    return False

"""THNodeGene is a representation of a Node Gene"""
class THNodeGene:
    localID: int
    nodeID: int
    keyID: str
    isInput = False
    isOutput = False

    incoming: []

    screenPosX: int
    screenPosY: int
    value = 0
    hasVal = False

    def __init__(self, nodeID, keyID, isInput, isOutput):
        self.nodeID = nodeID
        self.keyID = keyID
        self.isInput = isInput
        self.isOutput = isOutput
        self.incoming = []

    def printNodeGene(self):
        if(self.isOutput):
            print(self.keyID)
        else:
            print(self.localID)

    def HasVal(self):
        return self.hasVal

    def IsInput(self):
        return self.isInput

    def IsOutput(self):
        return self.isOutput


"""THConnGene is a representation of a Connection Gene"""
class THConnGene:
    innovationID: int
    input: THNodeGene
    output: THNodeGene
    weight: float
    isEnabled: bool

    def __init__(self, input, output, weight, isEnabled):
        self.innovationID = findInnovation(input, output)
        self.input = input
        self.output = output
        self.weight = weight
        self.isEnabled = isEnabled
        if(self.innovationID == NNDatabase.innovationID and connExists(input, output) == False):
            NNDatabase.connGenes.append(self)

    def printConnGene(self):
        print("InnovationID: " + str(self.innovationID))
        self.input.printNodeGene()
        print("->")
        self.output.printNodeGene()
        print("\n")

    def disable(self):
        self.isEnabled = False

    def enable(self):
        self.isEnabled = True

    def isEnabled(self):
        return self.enabled

    """def setWeight(self, w):
        self.weight = w

    def getInput(self):
        return self.input

    def getOutput(self):
        return self.output

    def getInnovationID(self):
        return self.innovationID"""

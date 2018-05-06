# newConn.printConnGene()

# print(numConns)
# print(newNetwork)
# newNetwork.printTHNetwork()


# print(inputID)
# print(outputID)

# print(NNDatabase.innovationID)

# evaluate w/ debug statements
    def evaluate(self, inputArr):

        tempNodes = []
        tempConns = []

        tempNodes = list(self.nodeGenes)
        tempConns = list(self.connGenes)

        """for i in range(0, len(tempNodes)):
            print(tempNodes[i].localID)

        for i in range(0, len(tempConns)):
            tempConns[i].printConnGene()"""

        for i in range(0, len(tempNodes)):
            if(tempNodes[i].IsInput() == True):
                tempNodes[i].val = inputArr[tempNodes[i].screenPosX][tempNodes[i].screenPosY] #sets the value of tempNodes to
                                                                                            # the normalized value of inputArr
                tempNodes[i].hasVal = True; #Don't have to worry about setting to false since tempNodes is a copy

        """for i in range(0, len(tempNodes)):
            s = "LocalID: " + str(i) + " val: " + str(tempNodes[i].val)
            print(s)"""


        i = 0
        while i < len(tempNodes):

            #print(len(tempNodes))
            #print(len(tempNodes[i].incoming))
            #print(i)

            if(tempNodes[i].isInput): i += 1; continue

            canEvaluate = True #if the incoming array is not empty, you can evaluate

            for j in range(0, len(tempNodes[i].incoming)):
                if(tempNodes[i].incoming[j].hasVal == False):
                    canEvaluate = False

            #print(tempNodes[i].localID)
            #print(canEvaluate)
            #print(tempNodes[i].hasVal)

            if(canEvaluate):
                tempNodes[i].val = 0

                # add all inputs, then apply activation function at the end
                for j in range(0, len(tempConns)):
                    if(tempConns[j].isEnabled and tempNodes[i].localID == tempConns[j].output.localID):
                        #evaluate tempNodes[i]
                        tempNodes[i].val = tempNodes[i].val + tempConns[j].input.val

                tempNodes[i].hasVal = True
                #print(tempNodes[i].val)
                #need activation code here

            else:

                #print("How often does it reach here?")
                """tempNodes[i].localID = len(tempNodes)  # tempNodes are out of scope from NodeGene[] nodes
                                                        # this changes the relative position of tempNodes

                for j in range(0, len(tempConns)):
                    if(tempNodes[i].localID == tempConns[j].input.localID): #update localID for each conn
                        tempConns[j].output.localID = tempNodes[i].localID"""

                #print(i)
                """for j in range(0, len(tempNodes[i].incoming)):  # update localID for each conn
                        print(tempNodes[i].incoming[j].localID)
                        print(tempNodes[i].incoming[j].hasVal)
"""
                tempNodes.append(tempNodes[i])
                tempNodes.pop(i)
                i -= 1

            i += 1
            #print(tempNodes[i].hasVal)

        """print("\nEND:")
        print(len(tempNodes))
        for j in range(0, len(tempNodes)):
            print(tempNodes[j].localID)
            print(tempNodes[j].hasVal)"""

        """for i in range(0, len(tempNodes)):
            if(tempNodes[i].hasVal):
                s = "LocalID: " + str(tempNodes[i].localID) + " val: " + str(tempNodes[i].val) + " lenIncoming: " + str(len(tempNodes[i].incoming))
                print(s)"""

        """for i in range(0, len(tempConns)):
            if (tempConns[i].output.hasVal):
                s = "OutputLocalID: " + str(tempConns[i].output.localID) + \
                    " val: " + str(tempConns[i].output.val) + " lenIncoming: " + str(len(tempConns[i].output.incoming))
                print(s)"""

        outputs = []
        for i in range(0, len(tempNodes)):
            if(tempNodes[i].isOutput and tempNodes[i].hasVal):
                outputs.append(tempNodes[i])


        #return the list of outputs - iterate through tempNodes[] and retrieve the output nodes

        return outputs

#getter/setters for THNetwork
"""def getNodeGenes(self):
    return self.nodeGenes

def getConnGenes(self):
    return self.connGenes

def getSpeciationID(self):
    return self.speciationID

def getGenomeID(self):
    return self.genomeID

def getNumConnGenes(self):
    return self.numConns

def getNumNodeGenes(self):
    return self.numNodes

def getFitness(self):
    return self.fitness"""


#getters/setters for THNodeGene
"""def setLocalID(self, id):
    self.localID = id

def setHVal(self, s):
    self.hasVal = s

def setVal(self, v):
    self.value = v

def setScreenPosX(self, x):
    self.screenPosX = x

def setScreenPosY(self, y):
    self.screenPosY = y

def getNodeID(self):
    return self.nodeID

def getLocalID(self):
    return self.localID

def getVal(self):
    return self.value

def getIncoming(self):
    return self.incoming

def getScreenPosX(self, x):
    return self.screenPosX

def getScreenPosY(self, y):
    return self.screenPosY"""

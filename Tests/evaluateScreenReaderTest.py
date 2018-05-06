import os
from Controller import Controller
from NEATAlgorithm import GeneratePopulation
from NEATAlgorithm import THNetwork
from NEATAlgorithm import THGene
from NNData import NNDatabase

GeneratePopulation.generateNodes(84, 98)

testNetwork = THNetwork.THNetwork(0, 0)

#create nodes
input1 = NNDatabase.inputs[10][35]
input2 = NNDatabase.inputs[53][65]
input3 = NNDatabase.inputs[61][45]

hidden1 = THGene.THNodeGene(0, "hidden", False, False)

output1 = NNDatabase.outputs[3]
output2 = NNDatabase.outputs[0]


#add nodes
testNetwork.addNodeGene(input1)
testNetwork.addNodeGene(input2)
testNetwork.addNodeGene(input3)
testNetwork.addNodeGene(output1)
testNetwork.addNodeGene(hidden1)
testNetwork.addNodeGene(output2)


#create conns
conn1 = THGene.THConnGene(testNetwork.nodeGenes[0], testNetwork.nodeGenes[3], 0.7, True)
conn2 = THGene.THConnGene(testNetwork.nodeGenes[1], testNetwork.nodeGenes[3], 0.5, False)
conn3 = THGene.THConnGene(testNetwork.nodeGenes[2], testNetwork.nodeGenes[3], 0.5, True)
conn4 = THGene.THConnGene(testNetwork.nodeGenes[1], testNetwork.nodeGenes[4], 0.2, True)
conn5 = THGene.THConnGene(testNetwork.nodeGenes[4], testNetwork.nodeGenes[3], 0.4, True)
conn6 = THGene.THConnGene(testNetwork.nodeGenes[0], testNetwork.nodeGenes[4], 0.6, True)
conn7 = THGene.THConnGene(testNetwork.nodeGenes[0], testNetwork.nodeGenes[5], 0.8, True)
conn8 = THGene.THConnGene(testNetwork.nodeGenes[4], testNetwork.nodeGenes[5], 1, True)

#add conns
testNetwork.addConnGene(conn1)
testNetwork.addConnGene(conn2)
testNetwork.addConnGene(conn3)
testNetwork.addConnGene(conn4)
testNetwork.addConnGene(conn5)
testNetwork.addConnGene(conn6)
testNetwork.addConnGene(conn7)
testNetwork.addConnGene(conn8)


#modify incoming[] fields of NodeGenes to
for i in range(0, testNetwork.numConns):
    #print(testNetwork.connGenes[i].isEnabled)
    if(testNetwork.connGenes[i].isEnabled):
        testNetwork.nodeGenes[testNetwork.connGenes[i].output.localID].incoming.append(testNetwork.connGenes[i].input)

inputArr = []
for i in range(0, 84):
    tempArr = []
    for j in range(0, 98):
        tempArr.append(1)

    inputArr.append(tempArr)

NNDatabase.population.append(testNetwork)

Controller.runController()

"""#while(1):
outputArr = testNetwork.evaluate(inputArr)
#    print(outputArr)

print(outputArr)

for i in range(0, len(outputArr)):
    outputArr[i].printNodeGene()
    print(outputArr[i].val) """
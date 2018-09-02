import os
from Controller import Controller
from NEATAlgorithm import GeneratePopulation
from NEATAlgorithm import THNetwork
from NEATAlgorithm import THGene
from NNData import NNDatabase

GeneratePopulation.generateNodes(84, 98)

#NETWORK 1
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

#testNetwork.mutateAddNode()
#testNetwork.mutateAddConn()
#testNetwork.printTHNetwork() #make print return valuable inf

species0 = []
species0.append(testNetwork)
NNDatabase.population.append(species0)

"""---------------------------------------------------------------------------------------------------------------------"""

# NETWORK 2
testNetwork2 = THNetwork.THNetwork(1, 0)

#create nodes
input1 = NNDatabase.inputs[40][13]
input2 = NNDatabase.inputs[20][90]
input3 = NNDatabase.inputs[10][20]

hidden1 = THGene.THNodeGene(0, "hidden", False, False)

output1 = NNDatabase.outputs[3]
output2 = NNDatabase.outputs[0]


#add nodes
testNetwork2.addNodeGene(input1)
testNetwork2.addNodeGene(input2)
testNetwork2.addNodeGene(input3)
testNetwork2.addNodeGene(output1)
testNetwork2.addNodeGene(hidden1)
testNetwork2.addNodeGene(output2)

#create conns
conn1 = THGene.THConnGene(testNetwork.nodeGenes[0], testNetwork.nodeGenes[3], 0.4, True)
conn2 = THGene.THConnGene(testNetwork.nodeGenes[1], testNetwork.nodeGenes[3], 0.1, False)
conn3 = THGene.THConnGene(testNetwork.nodeGenes[2], testNetwork.nodeGenes[3], 0.7, True)
conn4 = THGene.THConnGene(testNetwork.nodeGenes[1], testNetwork.nodeGenes[4], 0.5, True)
conn5 = THGene.THConnGene(testNetwork.nodeGenes[4], testNetwork.nodeGenes[3], 0.8, True)
conn6 = THGene.THConnGene(testNetwork.nodeGenes[0], testNetwork.nodeGenes[4], 0.6, True)
conn7 = THGene.THConnGene(testNetwork.nodeGenes[0], testNetwork.nodeGenes[5], 0.9, True)
conn8 = THGene.THConnGene(testNetwork.nodeGenes[4], testNetwork.nodeGenes[5], 1, True)

conn9 = THGene.THConnGene(testNetwork.nodeGenes[0], testNetwork.nodeGenes[1], 0.4, True)
conn10 = THGene.THConnGene(testNetwork.nodeGenes[2], testNetwork.nodeGenes[4], 0.2, True)
conn11 = THGene.THConnGene(testNetwork.nodeGenes[1], testNetwork.nodeGenes[2], 0.7, True)

#add conns
testNetwork2.addConnGene(conn1)
testNetwork2.addConnGene(conn2)
testNetwork2.addConnGene(conn3)
testNetwork2.addConnGene(conn4)
testNetwork2.addConnGene(conn5)
testNetwork2.addConnGene(conn6)
testNetwork2.addConnGene(conn7)
testNetwork2.addConnGene(conn8)

testNetwork2.addConnGene(conn9)
testNetwork2.addConnGene(conn10)
testNetwork2.addConnGene(conn11)

#modify incoming[] fields of NodeGenes to
for i in range(0, testNetwork2.numConns):
    #print(testNetwork2.connGenes[i].isEnabled)
    if(testNetwork2.connGenes[i].isEnabled):
        testNetwork2.nodeGenes[testNetwork2.connGenes[i].output.localID].incoming.append(testNetwork2.connGenes[i].input)

inputArr = []
for i in range(0, 84):
    tempArr = []
    for j in range(0, 98):
        tempArr.append(1)

    inputArr.append(tempArr)

#testNetwork.mutateAddNode()
#testNetwork.mutateAddConn()
#testNetwork.printTHNetwork() #make print return valuable inf

species1 = []
species1.append(testNetwork)
NNDatabase.population.append(species1)

"""for i in range(0, len(NNDatabase.population)):
    print(NNDatabase.population[i])

print(len(NNDatabase.population))"""

Controller.crossover(testNetwork, testNetwork2)
print(len(NNDatabase.population))

testNetwork.printTHNetwork()
testNetwork2.printTHNetwork()
NNDatabase.population[0][1].printTHNetwork()

#while(1):
#outputArr = testNetwork.evaluate(inputArr)
#    print(outputArr)

"""print(outputArr)

for i in range(0, len(outputArr)):
    outputArr[i].printNodeGene()
    print(outputArr[i].val)"""

"""from NEATAlgorithm import GeneratePopulation
from NNData import NNDatabase

GeneratePopulation.generateNodes(84, 98)

#print(len(NNDatabase.inputs))
#print(len(NNDatabase.outputs))

#population = []
population = GeneratePopulation.generatePopulation(5)

for i in range(0, len(population)):
    population[i].printTHNetwork() #make print return valuable info

print(len(NNDatabase.connGenes))"""
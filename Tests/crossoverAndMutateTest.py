from NEATAlgorithm import GeneratePopulation
from NNData import NNDatabase
from Controller import Controller

#GeneratePopulation.generateNodes(84, 98)

#print(len(NNDatabase.inputs))
#print(len(NNDatabase.outputs))

#population = []
#population = GeneratePopulation.generatePopulation(5)


"""for i in range(0, len(population)):
    population[i][0].printTHNetwork() #make print return valuable info"""

Controller.runController()

#print(len(NNDatabase.connGenes))
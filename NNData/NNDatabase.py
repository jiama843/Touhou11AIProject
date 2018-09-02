#This file will store data using with variables and handle it using I/O files

innovationID = 0 # Technically starts at 1 due to THConnGene init
maxFitness = 0

fitnessThreshold: int #This will decide if the network is optimized

population = [] #Networks list. Will be a list of lists: [[]]
inputs = [] #list of input nodeGenes (8232 of them) ([[]]) ////////////Not (1521 of them)
outputs = [] #list of output nodeGenes (4 of them)
nodeGenes = []
connGenes = [] # Keep track of innovations
speciationIDs = []

numSpecies: int
numConnGenes: int
numNodeGenes: int
numNetworks: int

compatDistThreshold: int

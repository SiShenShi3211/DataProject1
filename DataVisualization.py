"""
Programmer: William Stobaugh, 9/9/21
Application: A practice on reading data from files
"""
#import other classes
from graph import Graph
from node import Node
from dataReader import Reader
from matplotlib import pyplot as plt


#init variables
heartFileReader = Reader("heartFailureDataset.csv")
heartFailureGraph = Graph("Heart Failure", ([]), heartFileReader.getTypes())

heartDiseaseReader = Reader("heartDiseaseDataset.csv")
heartDiseaseGraph = Graph("Heart Disease", ([]), heartDiseaseReader.getTypes())



###########################       METHODS        #####################
#Read from file and append to data, in tuple form (x,y)



###################################################################

#run functions
#testGraph.drawGraph()
#heartFileReader.getTypeIndex("platelets")
#testGraph.printTypes()


heartFileReader.addDataToGraph(heartFailureGraph)
#heartFailureGraph.plot("age", "platelets")
# heartFailureGraph.makePieChart("anaemia")
heartFailureGraph.formatData()
heartFailureGraph.sortNodes("age")
# heartFailureGraph.formatData()
heartFailureGraph.makePieChart("DEATH_EVENT")

#heartDiseaseReader.addDataToGraph(heartDiseaseGraph)
#heartDiseaseGraph.formatData()
#heartDiseaseGraph.plot("age", "fbs")
#heartDiseaseGraph.makePieChart("sex")



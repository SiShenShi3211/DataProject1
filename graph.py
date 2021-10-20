#graphics for visual representation
from graphics import *
from matplotlib import pyplot as plt
import numpy as np
from node import Node

#graph object in  data, should have a name and contain multiple nodes of data
class Graph:
    #init function
    def __init__(self, name, nodes, requirements):
        self.name = name
        self.nodes = nodes
        self.requirements = requirements
    

    #function for printing inside nodes
    def printData(self):
        for node in self.nodes:
            print(node.data)

    #function to display type names in each coloumn
    def printTypes(self):
        print(self.requirements)
    
    def makePieChart(self, title):
        #logic: iterate through all the data in specific type, check if it is different from existing values
        # if so then make another name and size for it

        #variable to hold tuples (name, size)
        storage = []
        #for every node and data
        for node in self.nodes:
            for pair in node.data:
                #if requested type...
                if title == pair[0]:
                    #variable to check if in array
                    inArray = False
                    #check if in names array already
                    for block in storage:
                        #if the value exists in name...
                        if block[0] == pair[1]:
                            #make true so we dont make a new catagory
                            inArray = True
                            # Add one to the size
                            y = list(block)
                            y[1] += 1
                            storage.remove(block)
                            storage.append(tuple(y))
                            

                    if inArray == False:
                        #if not existant append another tuple inside of storage
                        storage.append((pair[1], 1))
                        
        #print(storage)
        # Print the pie chart using the storage

        #get names and sizes
        names = []
        sizes = []
        for pair in storage:
            names.append(str(pair[0]) + ": " + str(pair[1]))
            sizes.append(pair[1])

        #show plot
        plt.pie(sizes, labels=names)
        plt.title = title
        plt.show()
                    
        

    #function which takes the two values of its data and then compares them with a plot
    def plot(self, xTitle, yTitle):
        #make array for values
        xValues = []
        yValues = []

        #put values inside of arrays
        for node in self.nodes:
            for pair in node.data:
                if (pair[0] == xTitle):
                    #print("X data added...")
                    xValues.append(float(pair[1]))
                if (pair[0] == yTitle):
                    #print("Y data added...")
                    yValues.append(float((pair[1]).rstrip()))  

        #use arrays to make plot

        #sort x values to actually make sense
        xValues.sort()
        
        #plot data
        plt.plot(xValues, yValues)

        # calc the trendline
        z = np.polyfit(xValues, yValues, 1)
        p = np.poly1d(z)
        plt.plot(xValues,p(xValues),"r--")

        #x min and max should be the first and last indexes in x values
        plt.xlim(xValues[1], xValues[len(xValues) - 1])

        #render graph
        plt.show()

    #function for formatting
    def formatData(self):
        #logic
        """
        1. Print each type
        2. print each piece of data
        """
        #PRINT TYPES
        for title in self.requirements:
            print(title + "    ", end="")
        print("")
        #PRINT DATA
        for node in self.nodes:
            for pair in node.data:
                print(pair[1], "    ", end="")
            print("")
    
    #function to add another node
    def addNode(self, node):
        self.nodes.append(node)

    #function for sorting list of nodes based on title and type of data
    def sortNodes(self, sortedTitle):
        #logic for each node, sorted title is the x value of a certain node we are looking for
        """
        1. make new array of nodes (sorted)
            1.a Iterate through each node, make tuple (x: title value, y: node)
            1.b Sort nodes from highest to lowest with python sorting
        2. clear nodes of graph and replace with those
        """
        tuples = []
        #for every node and data, add values to tuples array
        for node in self.nodes:
            for pair in node.data:
                #if requested type...
                if sortedTitle == pair[0]:
                    #add tuple to
                    tuples.append((pair[1], Node(node.data).data))

        
        #clear nodes in graph
        self.nodes = []

        #sort tuples
        tuples.sort(key=lambda tup: tup[0])  # sorts in place

        #add nodes from tuples
        for pair in tuples:
            self.nodes.append(Node(pair[1]))
            #print(pair[0] , "    ", pair[1])




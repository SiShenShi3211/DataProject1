from node import Node
#class which attributes to a column on a graph, should contain boxes with name and data
class Reader():

    #Initilize itself
    def __init__(self, file):
        self.file = file
    
    #Method to return types
    def getTypes(self):
        with open(self.file) as f:
            lines = f.read() ##Assume the sample file has 3 lines
            first = lines.split('\n', 1)[0]
            types = first.split(',')
            return types
    
    #Method which gets index of a title
    def getTypeIndex(self, title):
        index = 0
        for typeName in self.getTypes():
            if (title == typeName):
                print(index)
                return index
            index += 1
    
    #Method which adds data from file to graph object
    def addDataToGraph(self, graph):
        #create node from each line starting at 2
        #Data should be in the (x: Index of graph.requirements, y: value index in file)
        with open(self.file) as f:
            #skip first line which has data types
            next(f)
            #iterate through each line
            for line in f:
                #split line into array to get y values
                values = line.split(',')
                types = self.getTypes()
                tupleArray = []
                
                index = 0
                #for each type fill it in with a value
                for title in types:
                    tupleArray.append((title, values[index]))
                    index += 1

                #add node to graph
                graph.addNode(Node(tupleArray))
                
        
        


class Vertex:
    def __init__(self,key,weight):
        self.id = key
        self.course_time = weight
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connectedTo:'  + str([x.id for x in self.connectedTo]) 

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getCourse_time(self):
        return self.course_time

    def getWeight(self,nbr):
        return self.connectedTo[nbr] 

      
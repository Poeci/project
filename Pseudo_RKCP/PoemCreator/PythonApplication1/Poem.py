import Stanza
import sys # uzywane do printowania bez entera xDD
from random import randint

class Poem(object):
    """description of class"""
    stanzas = []
    numberOfSyllabesInEachStanza = int

    def __init__(self, howLong, graph, dictionary):
        self.howLong = howLong
        self.graph = graph
        self.dictionary = dictionary
        self.resultWords = []
        self.resultSigns = []
        self.visitedBy = {}


    def Dfs(self, currentWord, size):
        if size == self.howLong:
            self.resultWords[size-1] = currentWord
            return True

        numberOfNeighbors = len(self.graph[currentWord])
        for i in range (0, 2*numberOfNeighbors-1):
            randomNumberOfNeighbour = randint(0, numberOfNeighbors-1)
            neighbor = self.graph[currentWord][randomNumberOfNeighbour][0]
            sign = self.graph[currentWord][randomNumberOfNeighbour][1]
              #     if self.visitedBy[neighbor]!=currentWord:
            if self.visitedBy.get(neighbor, "!@#nothin")!=currentWord:  
                self.visitedBy[neighbor] = currentWord
                if self.Dfs(neighbor, size+1):
                    self.resultWords[size-1] = currentWord
                    self.resultSigns[size-1] = sign
                    return True
        return False


    def Generate(self, firstWord):
        self.resultWords = [None] * self.howLong
        self.resultSigns = [None] * self.howLong
       # self.visitedBy = [None] * self.howLong
        self.resultWords[self.howLong-1] = -1
        self.Dfs(firstWord, 1)  

        if self.resultWords[self.howLong-1] == -1:
            return False
        
        for i in range(0, self.howLong-1):
		    wordWithSign = (self.dictionary[self.resultWords[i]] + self.resultSigns[i]).encode('utf-8')
		    sys.stdout.write(wordWithSign)
        print ('\n')
        return True



        

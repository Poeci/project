# -*- coding: utf-8 -*-
import Stanza
from collections import defaultdict
import sys # uzywane do printowania bez entera, encoding
from random import randint
import codecs

class Poem(object):
    """description of class"""

    def __init__(self, howLong, graph):
        self.howLong = howLong
        self.graph = graph
        self.resultWords = []
        self.resultSigns = []
        self.visitedBy = {}

    def Dfs(self, currentWord, size):
        if size == self.howLong:
            self.resultWords[size-1] = currentWord
            return True

        numberOfNeighbors = len(self.graph[currentWord])
        for i in range (0, 2*numberOfNeighbors-1):
            randomNumberOfNeighbor = randint(0, numberOfNeighbors-1)
            neighbor = self.graph[currentWord][randomNumberOfNeighbor][0]
            sign = self.graph[currentWord][randomNumberOfNeighbor][1]
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
        self.resultWords[self.howLong-1] = -1
        self.Dfs(firstWord, 1)  

        if self.resultWords[self.howLong-1] == -1:
            return False
        
        for i in range(0, self.howLong-1):
            wordWithSign = (self.resultWords[i] + self.resultSigns[i]).encode("utf-8")
            sys.stdout.write(wordWithSign)
        print ('\n')
        return True



        

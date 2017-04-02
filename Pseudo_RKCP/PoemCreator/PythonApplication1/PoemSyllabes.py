#!/usr/bin/python
# -*- coding: utf-8 -*-
import Stanza
from collections import defaultdict
import sys # uzywane do printowania bez entera, encoding
from random import randint, choice
import codecs
import Dictionary as d

class PoemSyllabes(object):
    """description of class"""

    def __init__(self, numberOfStanzas, graph, syllabes):
        self.numberOfStanzas = numberOfStanzas
        self.graph = graph
      #  self.resultWords = []
      #  self.resultSigns = []
       # self.visitedBy = {}
        self.syllabes = syllabes
        self.resultWords = defaultdict(list)
        self.resultSigns = defaultdict(list)
        self.visitedBy = defaultdict(list)
        self.vowels = [u'a', u'e', u'i', u'o', u'u', u'y', u'ą', u'ę', u'ó']
        self.MAX = 2000;


    def GetNumberOfSyllabes(self, word):
        number = 0
        #word = word.decode(sys.stdin.encoding)
        for i in range(0, len(word)):
            if word[i] in self.vowels:    
                number+=1
                if i<len(word)-1 and word[i]==u'i' and (word[i+1] in self.vowels):
                    number-=1
        return number

    def Dfs(self, currentWord, size, numberOfStanza, allSyllabes):
        currentWordSyllabes = self.GetNumberOfSyllabes(currentWord)
        allSyllabes+=currentWordSyllabes
        if self.syllabes==allSyllabes:
            self.resultWords[numberOfStanza][size-1] = currentWord
            return True

        neighbors = d.GetNeighbors(currentWord)
        numberOfNeighbors = len(neighbors)
        for i in range (0, 2*numberOfNeighbors-1):
            randomNumberOfNeighbor = randint(0, numberOfNeighbors-1)
            neighbor = neighbors[randomNumberOfNeighbor]
            sign = ' ';
            newSyllabes = self.GetNumberOfSyllabes(neighbor)
            if sign=='\n' or newSyllabes+allSyllabes>self.syllabes: continue ## nie chcemy brac nowej linii
            if self.visitedBy[numberOfStanza].get(neighbor, "!@#nothin")!=currentWord:  
                self.visitedBy[numberOfStanza][neighbor] = currentWord
                if self.Dfs(neighbor, size+1, numberOfStanza, allSyllabes):
                    self.resultWords[numberOfStanza][size-1] = currentWord
                    self.resultSigns[numberOfStanza][size-1] = sign
                    return True
        return False

    def GetFirstWord(self):
        while True: #for i in range(0, len(graph)-1):
            firstWord = choice(self.graph.keys())
            for i in range(0, len(self.graph[firstWord])):
                if self.graph[firstWord][i][1]=='\n':             
                    return self.graph[firstWord][i][0]

    def Generate(self):
        for i in range(0, self.numberOfStanzas):
            firstWord = self.GetFirstWord()
            self.resultWords[i] = [None] * self.MAX
            self.resultSigns[i] = [None] * self.MAX
            self.resultWords[i] = [-1] * self.MAX 
            self.visitedBy[i] = {}
            self.Dfs(firstWord, 1, i, 0)
            if self.resultWords[i][0]==-1: 
                i-=1
                continue
           # self.resultWords[i][0][0] = self.resultWords[i][0][0].upper()
            lastWasDot = False
            for x in range(0, self.MAX):
                if (self.resultWords[i][x+1]==-1): break
                wordWithSign = (self.resultWords[i][x] + self.resultSigns[i][x])#.encode("utf-8")
                lastWasDot = self.resultSigns[i][x]=='.'
                sys.stdout.write("".join(c.upper() if (i == 0 and x == 0) or lastWasDot else c for i, c in enumerate(wordWithSign)))#.encode("utf-8"))))
            sys.stdout.write(self.resultWords[i][x])#.encode("utf-8"))
            r = randint(0, 1)
            if r==1 or i==self.numberOfStanzas-1: print('.')
            else: print (',')
   
        return True



        

# -*- coding: utf-8 -*-
from collections import defaultdict
import codecs
from Poem import Poem
from random import randint, choice

graph = defaultdict(list)
dictionary = {}
lineIndex = 0
lines = []

def GetConnectionType(number):
    switcher = {
        '0' : " ",
		'1' : ", ",			
		'2' : ". ",			
		'3' : "\n",
		'4' : "...",	
		'5' : "? ",
		'6' : "! ",
		'7' : " - ",
		'8' : ": ",
		'9' : " ",
    }
    return switcher.get(number, " ") # drugi argument jest opcja defaultowa

def InputGraph():
    while True:
        global lineIndex
        line = lines[lineIndex]   
        lineIndex+=1
        if line=='<END>':
            break
        elements = line.split(" ")
        if (len(elements)==3): # jebane podwojne spacje, w wierszach czesto wystepowaly :/    
            wordFrom = elements[0]
            wordTo = elements[1]
            connectionType = GetConnectionType(elements[2])
            graph[wordFrom].append((wordTo, connectionType));


def ReadFromFile(fileName):
    print('Reading from file: '+fileName)
    reader = codecs.open(fileName, encoding='utf-8')
    for line in reader:
        goodLine = line.rstrip() #rstrip usuwa znaki \n na koncach
        goodLine = goodLine.replace(u'\ufeff', '')
        lines.append(goodLine)  

print("Reading from files...")
ReadFromFile('graphPoems.txt')
ReadFromFile('graphTadeusz.txt')
lines.append('<END>')

print("Making graph...")
InputGraph()

print("Ready! Type enter to make poem")

while True:
    raw_input()
    newPoem = Poem(30, graph)
    for i in range(0, len(graph)-1):
        firstWord = choice(graph.keys())
        if (newPoem.Generate(firstWord)):
            break

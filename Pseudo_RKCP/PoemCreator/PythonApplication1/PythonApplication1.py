from collections import defaultdict
import codecs
from Poem import Poem
from random import randint

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
        numberFrom = int(elements[0])
        numberTo = int(elements[1])
        if numberFrom!=173 and numberTo!=173: # jebane podwojne spacje, w wierszach czesto wystepowaly :/    
            connectionType = GetConnectionType(elements[2])
            graph[numberFrom].append((numberTo, connectionType));

def InputDefinitionOfWords():
    while True:
        global lineIndex
        line = lines[lineIndex]
        if line=="<TYPES>":
            break
        lineIndex+=1
        elements = line.split(" ")
        if len(elements)==1:
            continue
        number = int(elements[0])
        word = elements[1]
        dictionary[number] = word

print("Making graph...")
    
reader = codecs.open('graph.txt', encoding='utf-8')
for line in reader:
    goodLine = line.rstrip() #rstrip usuwa znaki \n na koncach
    goodLine = goodLine.replace(u'\ufeff', '')
    lines.append(goodLine)  

InputGraph()
InputDefinitionOfWords()

print("Ready! Type enter to make poem")

while True:
    raw_input()
    newPoem = Poem(30, graph, dictionary)
    for i in range(0, len(dictionary)-1):
        tmp = randint(0, len(dictionary)-1)
        if (newPoem.Generate(tmp)):
            break






print dictionary[2]

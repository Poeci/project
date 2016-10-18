import xml.etree.cElementTree as ET
import codecs

def AddToAllWordsXml(word, basicForm, partOfSpech, grama, ID):
    wordElement = ET.SubElement(allWords, "word", name = word, id = str(ID))
    ET.SubElement(wordElement, "basicForm").text = basicForm
    ET.SubElement(wordElement, "partOfSpeech").text = partOfSpech
    ET.SubElement(wordElement, "grama").text = grama

def AddToBasicXml(basicForm, ID):
    cipa
    

f = codecs.open('dictionary.txt', 'r', 'utf8')
allWords = ET.Element("allWords")
allWordsTree = ET.ElementTree(allWords)

basicForms = ET.Element("basicForms")
basicFormsTree = ET.ElementTree(basicForms)
basicFormsMap = {}


ID = 0
for line in f:
    # print (line)
    basicParts = line.split(';')
    basicForm = basicParts[0]
    word = basicParts[1]

    if basicForm not in basicFormsMap: basicFormsMap[basicForm] = []
    basicFormsMap[basicForm].append(ID)

    gramaticParts = basicParts[2].split(':')
    partOfSpeech = gramaticParts[0]
    grama = basicParts[2]
    AddToAllWordsXml(word, basicForm, partOfSpeech, grama, ID)
    ID+=1


ID = 0
basicID = 0
for key, value in basicFormsMap.items():
    wordElement = ET.SubElement(basicForms, "word", name = key, id = str(basicID))
    for ID in value:
        ET.SubElement(wordElement, "ID").text = str(ID)
    basicID+=1

allWordsTree.write("allWords.xml")
basicFormsTree.write("basicForms.xml")


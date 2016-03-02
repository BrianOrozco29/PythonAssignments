'''
Brian Orozco
October 22nd, 2015
CS 100 H01

Homework 14 File HW
'''

#Question 4.27
def fcopy(inFile, outFile):
    rFile = open(inFile, 'r')
    cont = rFile.read()
    rFile.close()

    wFile = open(outFile, 'w')
    wFile.write(cont)
    wFile.close()

fcopy('testFile.txt', 'testFile2.txt')
print(open('testFile2.txt').read())


#Question 4.29
def stats(inFile):
    rFile = open(inFile, 'r')
    content = rFile.readlines()
    
    listFile = []
    for i in content:
        listFile += i.split()

    characters = 0

    for i in listFile:
        characters += len(i)

    rFile.close()

    print('Line count: ' + str(len(content)))
    print('Word count: ' + str(len(listFile)))
    print('Character count: ' + str(characters))


stats('testFile2.txt')

#Problem 3
import string

def repeatWords(inFile, outFile):
    inFile = open(inFile, 'r')     
    outFile = open(outFile, 'w')    
    
    for i in inFile:
        newList = []
        i = i.lower()         
        i = i.split(string.punctuation)     
    
        for word in i:           
            if i.count(word) >= 2 and word not in newList:     
                outFile.write(word + ' ')
                newList.append(word)        
            
        outFile.write('\n')

    inFile.close()
    outFile.close()

inFile = 'testFile2.txt'
outFile = 'output.txt'
repeatWords(inFile, outFile)

print(open(outFile).read())

        

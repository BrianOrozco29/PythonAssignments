'''
Brian Orozco
October 21st, 2015
CS 100 - H01

Homework 14
'''

import turtle

#Spring 2015 Midterm Problems
#Question 1
x = 2
for i in range(3):
    print(x, end = ' ')
    x += i
'''
My answer is c. 2 2 3
Correct answer: c.
'''

#Question 2
noise = 'hullaballoo'
idx = 0
while idx < len(noise):
    let = noise[idx]
    print(let, end='')
    letCount = noise.count(let)
    if idx > 2:
        idx += letCount
    else:
        idx += 1

'''
My answer is c. hulll
Correct Answer: c.
'''

#Question 3
s = 'GimmeASlice'
print(2*s[:5] + s[:])

'''
My answer is a. GimmeGimmeGimmeASlice
Correct answer: a.
'''

#Question 4
noise = 'hullaballoo'
changeCount = 0
for i in range(1, len(noise)):
    if noise[i] != noise[i-1]:
        changeCount += 1
print(changeCount)


'''
My answer is d. 7
Correct answer d.
'''

#Question 5
braveOnes = ['Merida', 'Elinor', 'Macintosh', 'Fergus']
vowels = 'aeiou'
for character in braveOnes:
    for vowel in vowels:
         if vowel in character:
             continue
         else:
             print(character[0], end='')
             break

'''
My answer is d. MEMF
Correct answer d.
'''

#Question 6
pandemics = [['HIV'], '', ['Ebola', 'SARS'], ['polio', 'smallpox']]
print(pandemics[1:3])


'''
My answer is e. none of the above
Correct answer: e
'''

#Skip Question 7

#Question 8
boolExprs = [True and False, not True, True or False, True and not False]
fCount = 0
for expr in boolExprs:
     if expr == False:
         fCount += 1
     else:
         break
print(fCount)

'''
My answer is c. 2
Correct answer: 2
'''

#Question 9
abe = 'no man has a good enough memory to be a successful liar'
def wordLens(t, limit):
     rtn = []
     aList = t.split()
     for s in aList:
         if len(s) > limit:
             return rtn
         rtn.append(len(s))
     return rtn
print(wordLens(abe, 5))

#Question 10
def fileCount(fileName, s):
     inF = open(fileName)
     count = 0
     for line in inF:
         count += line.lower().count(s)
     inF.close()
     return count
w = open('seuss.txt', 'w')
w.write('You have brains in your head' + '\n')
w.write('You have feed in your shoes' + '\n')
w.close()
print(fileCount('seuss.txt', 'you'))

'''
My answer is b. 4
Correct answer b.
'''

#Question 11a
t = turtle.Turtle()
s = turtle.Screen()

def halfSquare(t, length):
    for i in range(2):
        t.forward(length)
        t.left(90)

halfSquare(t, 100)
s.bye()

#11b
t = turtle.Turtle()
s = turtle.Screen()

def halfSquares(t, initial, increment, reps):
    for i in range(reps):
        halfSquare(t, initial)
        initial += increment

halfSquares(t, 25, 15, 10)

#Question 12
def wordCount(inFile,outFile):
    fileLines = inFile.readlines()
    
    newFile = []
    splitFile = []
    for i in range(len(fileLines)):
        splitFile += fileLines[i].split()
        newFile.append(len(splitFile))
    
    inFile.close()

    for i in newFile:
        outFile.write(str(i)+'\n')
    outFile.close()
    

inFile = open('humpty.txt','r')
outFile = open('output.txt','w')
wordCount(inFile,outFile)
        

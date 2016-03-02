'''
Brian Orozco
December 3rd, 2015
CS 100 H01

Final 2013
'''

#Question 6
order = [['1st', '2nd'], {'2nd': 'John', '1st': 'George'}, '1st', '2nd']
print(order[1]['1st'])

'''
My answer is e.
Correct answer: e.
'''

#Question 7
'''
presidents = {'Jefferson':3, 'Adams':2, 'Washington':1}
print(presidents[1])
'''

'''
My answer is d.
Correct answer: d.
'''

#Question 8
opVals = [not True, not not True, False and not True, not False and True]
falseCount = 0
for expr in opVals:
    if expr == False:
        falseCount += 1
print(falseCount)

'''
My answer is b.
Correct answer: b.
'''

#Question 9
'''
inF = open('thunder.txt', 'r')
outF = open('thunderOut.txt', 'w')
for line in inF:
    if 'we' in line.lower():
        outF.write(line)
inF.close()
outF.close()
'''

'''
My answer is b.
Correct answer: b.
'''

#Question 10
'''
from turtle import *
t = Turtle()
for i in range(4):
    if i%3 == 0:
        t.forward(100)
        t.right(90)
    elif i%2 == 0:
        t.forward(100)
    else:
        t.forward(100)
'''

'''
My answer is d.
Correct answer d.
'''

#Question 13
def vowelContent(wordList):
    d = {'mostly vowels': [], 'half vowels': [], 'mostly consonants': []}
    vowels = 'aeiou'
   
    for i in wordList:
        vowCount = 0
        for j in vowels:
            if j in i:
                vowCount += i.count(j)
        if vowCount > len(i) / 2:
            d['mostly vowels'].append(i)
        elif vowCount == len(i) / 2:
            d['half vowels'].append(i)
        elif vowCount < len(i) / 2:
            d['mostly consonants'].append(i)
            
    return d

list1 = ['Hopefully', 'this', 'code', 'works', 'because', 'it', 'would', 'be', 'bad', 'if', 'not']
print(vowelContent(list1))

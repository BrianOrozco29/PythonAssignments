'''
Brian Orozco
November 13, 2015
CS 100 - H01

Homework 18
'''

#Question 6
ben = "Lost time is never found again"		
def property(t):		
    tList = t.split()		
    d = {}		
    for word in tList:		
        length = len(word)		
        if len(word) not in d:		
            d[length] = 1		
        else:		
            d[length] += 1		
    return d

print(len(property(ben)))		

'''
My answer is e.
Correct answer: e.
'''

#Question 7
aDict = {1:'first int', 0:'zero'}
print(aDict[0])

'''
My answer is d.
Correct answer: d.
'''

#Question 8
bools = [True and not True, True or not True, not not True, not False, not True or False]
d = {True: 0, False: 0}
for expr in bools:
    if expr:
        d[True] += 1
        continue
    d[False] += 1
print(d)

'''
My answer is c.
Correct answer: c.
'''

#Question 9
import turtle
t = turtle.Turtle()
for i in range(2):
    if i%3 == 0:
            t.forward(100)
            t.left(120)
    if i%2 == 1:
        t.forward(100)
        t.left(120)
    elif i%3 == 0:
        t.forward(100)
        t.left(120)

'''
My answer is c.
Correct answer c.
'''

#Question 10
fishLine = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
indx = 0
while indx < len(fishLine):
    if len(fishLine[indx]) == 4:
        indx += 1
        continue
    indx += 5
print(indx)

'''
My answer is d.
Correct answer d.
'''

#Question 13
def symmetry(text):
    d= {}
    textLower = text.lower()
    textList = textLower.split()
    for i in textList:
        if i[0] == i[-1]:
            if i[0] not in d:
                d[i[0]] = 1
            else:
                d[i[0]] += 1
    return d

text = "Did this work I hope so because I would hate to do this all over again wow this is a long sentence"
print(symmetry(text))
        
    

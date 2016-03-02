'''
Brian Orozco
CS 100 H01
November 1st, 2015

Homework 16
'''

#Question 1
initial = 0
for i in range(7, 10):
     initial -= i
     print(initial, end = ' ')

'''
Correct answer: d
'''

#Question 2
refrain = 'HALLELUJAH'
countPattern = ''
for letter in refrain:
    count = refrain.count(letter)
    if str(count) in countPattern:
        countPattern += letter
    else:
        countPattern += str(count)
print(countPattern)

'''
Correct answer: c
'''

#Question 3
cypher = 'Kansas is going bye-bye'
print(cypher[-7:] + cypher[6:7] + cypher[:6])

'''
Correct answer e
'''

#Question 4
oldMacDonald = 'eieio'
equipment = 'radio receiver'
count = 0
for i in range(len(equipment)-1):
    substring = equipment[i:i+2]
    if substring in oldMacDonald:
        count += 1
print(count)

'''
Correct answer: b.
'''

#Question 5
def asymmetry(s):
    symmetric = ''
    for i in range(len(s)):
        if s[i] == s[-i-1]:
            symmetric += s[i]
        else:
            return s[i:-i]
    return symmetric
t = 'abcdba'
print(asymmetry(t))

'''
Correct answer: d.
'''

#Question 6
lst = [{'a':0,'z':25}, [2.7, 3.14], ['e', ['pi']]]
print(lst[2][1])

'''
Correct answer: c.
'''

#Question 7
def longWords(s, num):
    longList = []
    sList = s.lower().split()
    for word in sList:
        if len(word) >= num:
            longList.append(word)
    return longList
t = 'The ideas of the ruling class are the ruling ideas'
print(longWords(t, 5))

'''
Correct answer: b.
'''

#Question 8
d = {}
s = 'banana'
for letter in s:
    if letter not in d:
        d[letter] = 'odd'
    elif d[letter] == 'even':
        d[letter] = 'odd'
    else:
        d[letter] = 'even'
print(d)

'''
Correct answer: d.
'''

#Question 9
outF = open('digits.txt', 'w')
for i in range(10):
    outF.write(str(i))
outF.close()
inF = open('digits.txt', 'r')
print(inF.read())
inF.close()

'''
Correct answer a.
'''

#Question 10
'''
print(yesNo(3, 5, '=='))
def yesNo(a, b, comparison):
    if comparison == "==" and a == b:
        return 'Yes'
    elif comparison == '<' and a < b:
        return 'Yes'
    elif comparison == '>' and a > b:
        return 'Yes'
    else:
        return 'No'
'''

'''
Correct answer: e.
'''

#Question 11a
import turtle
t = turtle.Turtle()
s = turtle.Screen()

def outposts(t, radius, side):
        t.pendown()
        t.circle(radius)
        t.penup()
        t.fd(side)
        t.pendown()
        t.circle(radius)
        t.penup()
        t.left(90)
        t.fd(side)
        t.right(90)
        t.pendown()
        t.circle(radius)
        t.penup()
        t.left(180)
        t.fd(side)
        t.right(180)
        t.pendown()
        t.circle(radius)
        
outposts(t, 30, 100)    

s.bye()

#Question 11b
t = turtle.Turtle()
s = turtle.Screen()

def callPosts(t):
    t.pensize(5)
    outposts(t, 10, 50)

callPosts(t)

#Question 12
def descender(s):
    newList = []
    lst = s.split()
    for i in lst:
        if 'g' in i and i not in newList:
            newList.append(i)
        if 'j' in i and i not in newList:
            newList.append(i)
        if 'p' in i and i not in newList:
            newList.append(i)
        if 'q' in i and i not in newList:
            newList.append(i)
        if 'y' in i and i not in newList:
            newList.append(i)
    return newList

text = 'hopefully this works'
print(descender(text))

#Question 13
def wordLengths(inFile):
    d = {}
    inF = open(inFile, 'r')
    content = inF.readlines()
    
    for i in content:
        wordList = i.split(' ')
        
        for y in wordList:
            length = len(y.strip('\n !'))
            if length not in d:
                d[length] = 1
            else:
                d[length] += 1
    inF.close()
    return d
        
print(wordLengths('seuss.txt'))

    

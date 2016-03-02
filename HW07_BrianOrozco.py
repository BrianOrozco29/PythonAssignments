'''
Brian Orozco
September 29th, 2015
Homework 07
'''

#Question 1
trueCount = 0
if not True or False:
 trueCount += 1
elif True and not False:
 trueCount += 1
if True or False:
 trueCount += 1
elif not True or not False:
 trueCount += 1
else:
 trueCount +=1
print(trueCount)

'''
My answer is c. 2
Correct answer: 2
'''

#Question 2
aSeq = [-1, 0, 1, 2]
add = aSeq[-1] + aSeq[0] + aSeq[1]
print(add)


'''
My answer is b. 1
Correct answer: 1
'''

#Question 3
nested = [0, [], 1]
print(nested[0:1])


'''
My answer is b. [0]
Correct answer: [0]
'''

#Question 4
ints = [-2, -1, 0, 1, 2]
negative = ints[:2]
positive = ints[-2:]
print(negative + positive)


'''
My answer is c. [-2, -1, 1, 2]
Correct answer: c.
'''

#Question 5
'''
import turtle
s = turtle.Screen()
t = turtle.Turtle()
for i in range(4):
 if i//2 == 1:
    t.forward(100)
    t.right(90)
'''

'''
My answer is b. two adjacent sides of a square
Correct answer: b.
'''

#Question 6
def unbalanced(aList):
 for i in range(len(aList)):
     if aList[i] != aList[-i-1]:
         return aList[i]
mismatch = unbalanced([0, -1])
print(mismatch)

'''
My answer is b.
Correct answer: b.
'''

#Question 7
wishesWereFishes = True
wishesWereHorses = False
if wishesWereFishes:
 print('beggars would eat')
if wishesWereHorses:
 print('beggars would ride')
else:
 print('walk')

 
'''
My answer is b.
beggers would eat
walk
Correct answer: b.
'''

#Question 8
circleLetters = 'bdgopq'
reproach = 'bad dog'
accum = ''
for letter in reproach:
     if letter in circleLetters:
         accum += letter
print(accum)

'''
My answer is a. 'bddog'
Correct answer: a.
'''

#Question 9
def f(paramList):
 for element in paramList:
     if element == []:
         return 'emptyList'
     if element == '':
         return 'emptyString'
     return 'nonempty'
returnValue = f([[], '', 0])
print(returnValue)

'''
My answer is a. 'emptyList'
Correct answer: a.
'''

#Question 10
def plusAndMinus(sequence):
     returnVal = 0
     for num in sequence:
         returnVal += num
     return(returnVal)
print(plusAndMinus([-2, -1, 1, 2]))


'''
My answer is b. 0
Correct answer: b.
'''

"""
Question 11
Part A: 12 points
Write a function named dashes(). The function dashes() takes three
parameters:
1. a turtle, t
2. an integer, numDashes, that is the number of dashes that are drawn
3. an integer, dashLength, that is the length of each dash and also
 the length of the space between dashes
The function dashes() should use the turtle t to draw.
You should not make any assumptions about the initial up/down state,
position or orientation of t.
There is no specification about the state of the turtle on return from
dashes().
For example, for the function call
dashes(shelly, 10, 20)
the following is correct output

Question 11
Part B: 8 points
Write code that calls dashes(), using the parameter values in the
example in part A.
(Hint: before calling dashes(), you must import the turtle module and
create a turtle.)


Question 12 (20 points)
Write a function named shortest() that finds the length of the
shortest string in a list of strings.
The function shortest() takes one parameter:
1. a list of strings, textList
The function shortest() should return the length of the shortest
string in textList. You may assume that textList contains at least one
element (string).
For example, the following would be correct output:
>>> beatleLine = ['I', 'am', 'the', 'walrus']
>>> print(shortest(beatleLine))
1


Question 13 (20 points)
Write a function named nameHasLetter(). The function nameHasLetter()
takes one parameter
1. a string of length 1, aLetter
The function nameHasLetter() should
1. prompt the user and input the user’s name
2. print a message to the user saying whether or not their name
 contains aLetter
3. return True if the user’s name contains aLetter and False if it
 does not
For simplicity, you may treat an upper case letter as different from
the corresponding lower case letter (that is, there is no ‘t’ in
‘Thomas’).
For example, the following would be correct input and output:
>>> print(nameHasLetter('a'))
What is your name? Lily
Lily your name contains no a
False
Hint: The output “False” is printed after the function returns. The
two lines above “False” are printed while nameHasLetter() is
executing.
"""


#Question 11
import turtle
t = turtle.Turtle()
s = turtle.Screen()

def dashes(t, numDashes, dashLength):
    for i in range(numDashes):
        t.fd(dashLength)
        t.up()
        t.fd(dashLength)
        t.down()

dashes(t, 7, 15)

#Question 12
def shortest(textList):
    ans = len(textList[0])
    for i in range(len(textList)):
        if ans > len(textList[i]):
            ans = len(textList[i])

    return ans

textList1 = ['Hopefully', 'this', 'works']
print(shortest(textList1))

#Question 13
def nameHasLetter(aLetter):
    name = input("What's your name? ")
    for i in range(len(name)):
        if name[i] == aLetter:
            print(name + ", your name contains a(n) " + aLetter)
            return True

    print(name + ", your name contains no " + aLetter)
    return False

print(nameHasLetter("Q"))






















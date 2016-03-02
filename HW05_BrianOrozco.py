'''
Brian Orozco
September 23rd, 2015
CS 100 - H01

Homework 05
'''

"""
Multiple choice questions 1-10 (4 points each)
Question 1
boolsSeen = 0
bools = [not True, not False, True, False, True and False, True or False]
for expr in bools:
 if expr:
 boolsSeen += 1
print(boolsSeen)
# Hint: x += 1 is the same as x = x+1
a. SyntaxError: invalid syntax
b. 1
c. 2
d. 3
e. none of the above

Question 2
aSeq = [2, 1, 0, -1, -2]
sum = aSeq[0] + aSeq[-1] + aSeq[-2]
print(sum)
a. -1
b. 0
c. 1
d. 2
e. none of the above

Question 3
mix = ['zero', 0, ['two'], -1]
print(mix[0:-1])
a. [0, ['two']]
b. [0, ['two'], -1]
c. ['zero', 0, ['two']]
d. ['zero', 0, ['two'], -1]
e. none of the above

Question 4
aList = ['one', -1, 2]
prefix = aList[:2]
suffix = aList[-1:]
print(prefix + suffix)
a. ['one', -1, 2, -1, 2]
b. ['one', -1, -1, 2]
c. 1
d. [2, -1]
e. none of the above

Question 5
import turtle
s = turtle.Screen()
t = turtle.Turtle()
for i in range(4):
 if i%2 == 0:
 t.right(60)
 t.forward(100)
 t.right(60)
a. a straight line
b. two sides of a square
c. two sides of an equilateral triangle
d. an equilateral triangle
e. none of the above
"""


#Multiple Choice Questions (checked by pythontutor.org and IDLE)
'''
Problem 1. My answer: d. 3
Correct answer: d.
'''

'''
Problem 2. My answer: a. -1
Correct answer: a.
'''

'''
Problem 3. My answer: c. ['zero', 0, ['two']]
Correct answer: c.
'''

'''
Problem 4. My answer: e. None of the above
Correct answer: e.
'''

'''
Problem 5. My answer: c. two sides of an equilateral triangle
Correct answer: c.
'''

"""
Programming questions 11-13 (20 points each)
Question 11
Part A: 10 points
A tick is a short line that is used to mark off units of distance along a line.
Write a function named drawTick() that uses a turtle parameter to draw a single tick of specified
length perpendicular to the initial orientation of the turtle.
The function drawTick() takes two parameters:
1. a turtle, t, that is used to draw
2. an integer, tickLen, that is the length of the tick
When drawTick() is called, t is in the location that the first tick should be drawn. (Hint: remember
that the tick mark should be drawn perpendicular to the orientation that t is in when it is called.)
You should not make any assumptions about the initial up/down state of t.
On return from drawTicks(), t should be in the same location and have the same orientation that it
had when it was called.
Part B: 10 points
Write a function named drawTicks() that calls drawTick() repeatedly to draw a set of parallel tick
marks.
The function drawTicks() takes four parameters:
1. a turtle, t, that is used to draw
2. an integer, tickLen, that is the length of the tick
3. an integer, numTicks, that is the number of ticks to draw
4. an integer, distance, that is the distance between parallel tick marks
For example, the following would be correct output if drawTicks() were called by this code:
import turtle
s = turtle.Screen()
turt = turtle.Turtle()
drawTicks(turt, 5, 10, 15)
"""

#Programming Question 11
#Part A:

import turtle
s = turtle.Screen()
t = turtle.Turtle()
length = 30

def drawTick(t, tickLen):
    t.left(90)
    t.penup()
    t.fd(tickLen)
    t.right(180)
    t.pendown()
    t.fd(tickLen)
    t.left(90)
    return drawTick

drawTick(t, length)
s.bye()

#Part B
import turtle
s = turtle.Screen()
t = turtle.Turtle()

def drawTicks(t, tickLen, numTicks, distance):
    for i in range(numTicks - 1):
        drawTick(t, tickLen)
        t.penup()
        t.fd(distance)
    return drawTicks

drawTicks(t, 5, 10, 15)    

#Extra Challenge Problem
'''
Write a function that takes a integer parameter n
and returns a list of all integers less than n that can
be expressed as the sum of two different cubes.
'''
def cubeExpressions(n):
    list1 = []
    for num in range(n):
        if (num**3 + (num+1)**3) < n :
            list1.append((num**3 + (num+1)**3))

    return list1


print(cubeExpressions(10000))













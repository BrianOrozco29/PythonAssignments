'''
Brian Orozco
CS 100 H01
September 16th, 2015

Homework 03
'''

"""
1.	Write Python code that does the following:
i. Assigns the values 3, 4 and 5 to the variables a, b and c, respectively.
ii. Write an if statement that prints ‘OK’ if a is less than b
iii. Write an if statement that prints ‘OK’ if c is less than b
iv. Write an if statement that prints ‘OK’ if the sum of a and b is equal to c
v. Write an if statement that prints ‘OK’ if the sum of a squared and b squared equals c squared.
2.	Repeat the previous problem with the additional requirement that ‘NOT OK’ is printed if the condition is false.
3.	Write a program that asks the user for a color, a line width, a line length and a shape. Assume that the user will specify a that is either a line, a triangle, or a square. Use turtle graphics to draw the shape that the user requests of the size, color, line width and line length that the user requests.
"""

#1
a = 3
b = 4
c = 5
if a < b:
    print('OK')
if c < b:
    print('OK')
if a + b == c:
    print('OK')
if a**2 + b**2 == c**2:
    print('OK')
    
#2
if a < b:
    print('OK')
else:
    print('NOT OK')
    
if c < b:
    print('OK')
else:
    print('NOT OK')
    
if a + b == c:
    print('OK')
else:
    print('NOT OK')
    
if a**2 + b**2 == c**2:
    print('OK')
else:
    print('NOT OK')
    
#3
import turtle
s = turtle.Screen()
t = turtle.Turtle()

color = input("What color? ")
width = int(input("What line width? "))
length = int(input("What line length? "))
shape = input("Do you want a line, a triangle, or a square? ")

t.pencolor(color)
t.pensize(width)

if shape.lower() == 'line':
    t.forward(length)
    
elif shape.lower() == 'triangle':
    for i in range(3):
        t.forward(length)
        t.right(120)

elif shape.lower() == 'square':
    for i in range(4):
        t.forward(length)
        t.left(90)

else:
    print('User input error, please try again.')
        
    

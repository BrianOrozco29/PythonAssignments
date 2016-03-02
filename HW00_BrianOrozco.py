#Brian Orozco
#CS-100-H01
#HW 00, September 1, 2015

"""
1.	Log in to Moodle and post a brief message introducing yourself to the class (e.g., your interests, looking for a study partner, etc.). 
2.	Read the course syllabus.
3.	Install Python on your home computer.
4.	In the textbook: read Chapter 1 and Chapter 2.1 and 2.2
5.	In IDLE, create and save in a Python file that
a.	is named, if your name is Harry Houdini, for example, HW0_HarryHoudini.py and
begins with a comment containing your name, class and section, the date and number of the homework assignment. Use either a block comment or one-line comment style. E.g.

b.	has three assignment lines, each of which creates a variable (object) with a meaningful names and assigns it an int value. E.g., 
# Exercise 5b
months = 12

c.	has three assignment lines, each of which creates a variable (object) with a meaningful names and assigns it a float value. E.g., 
# Exercise 5c
height = 7.63
d.	has three assignment lines, each of which creates a string variable with a meaningful name. E.g., 
# Exercise 5d
manFromUncle = 'Napolean Solo'

6.	Do textbook exercises 
2.12 
2.13 
2.14 
2.15 
2.16 

"""

#Exercise 5b
years = 17
months = 11
days = 1

#Exercise 5c
hours = 19.5
height = 1.75
weight = 62.14

#Exercise 5d
metalGear = 'Big Boss'
pokemon = 'Charizard'
major = 'Comp Sci'

#Exercise 6 (textbook)
#2.12
s1 = '-'
s2 = '+'
#a
print(s1 + s2)
#b
print(s1 + s2 + s1)
#c
print(s2 + s1 +s1)
#d
print(s2 + (s1 * 2) + s2 + (s1 * 2))
#e
print(10 * (s2 + s1 + s1) + s2)
#f
print(5 * ((s2 + s1) + (3 * s2) + (2 * s1)))

#2.13
s = 'abcdefghijklmnopqrstuvwxyz'
print(s[0])
print(s[2])
print(s[25])
print(s[24])
print(s[16])

#2.14
s = 'goodbye'
#a
print(s[0] is 'g')
#b
print(s[6] is 'g')
#c
print(s[0] is 'g' and s[1] is 'a')
#d
print(s[5] is 'x')
#e
print(s[3] is 'd')
#f
print(s[0] is s[6])
#g
print(s[3] + s[4] + s[5] + s[6] is 'tion')

#2.15
#a
a = 'anachronistically'
b = 'counterintuitive'
print((len(a) - len(b)) == 1)
#b
words = ['misrepresentation', 'misinterpretation']
words.sort()
print(words)
#c
e = 'e'
print(e not in 'floccinaucinihilipilification')
#d
a = 'counterrevolution'
b = 'counter'
c = 'resolution'
print(len(a) == len(b + c))

#2.16
#a
a = 6
b = 7
#b
c = (a + b) / 2
#c
inventory = ['paper', 'staples', 'pencils']
#d
first = 'John'
middle = 'Fitzgerald'
last = 'Kennedy'
#e
fullname = first + " " + middle + " " + last

print(a)
print(b)
print(c)
print(inventory)
print(first)
print(middle)
print(last)
print(fullname)

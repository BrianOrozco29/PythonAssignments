'''
Brian Orozco
CS 100 H01
September 9th, 2015

Homework 01
'''

"""
1.	Read sections 2.3, 2.4 and 2.5 in the textbook
2.	Do textbook exercises 
2.18
2.19
2.21
3.	Assume that the variable grades is a list of the letters A, B, C, D, and F. For example,

grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A']

Write a Python expression that creates a list named frequency, in which the elements are the number of times each of the letters A, B, C, D and F appear in grades. For example, for the above value of grades, the following would be correct output.

frequency = [3, 1, 1, 0, 2]

Your expression must give the correct values for any list of grades, not just the one in this example. Hint: use the list method count.

"""

#Do textbook exercises

#2.18
#a
flowers = ['rose', 'bougainvilles', 'yucca', 'marigold', 'daylilly', 'lilly of the valley']
#b
print('potato' != flowers)
#c
thorny = [flowers[0], flowers[1], flowers[2]]
print(thorny)
#d
poisonous = [flowers[-1]]
print(poisonous)
#e
dangerous = thorny + poisonous
print(dangerous)

#2.19

answers = ['Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'N']
#a
numYes = answers.count('Y')
print(numYes)
#b
numNo = answers.count('N')
print(numNo)
#c
percentYes = (numYes / len(answers)) * 100
print(str(percentYes) + '%')
#d
answers.sort()
print(answers)
#e
f = answers.index('Y')
print(f)

#2.21

s = 'Orozco'
t = 'Brian'
initials = t[0] + s[0]
print(initials)

#3. List exercise
grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A']
frequency = [grades.count('A'), grades.count('B'), grades.count('C'), grades.count('D'), grades.count('F')]
print(frequency)

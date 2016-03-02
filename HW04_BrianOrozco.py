'''
Brian Orozco
September 20th, 2015
CS100 - H01

Homework 04
'''

#3.20
#Print 1st three chars of every word in a list
months = ['January', 'February', 'March']
for name in months:
    print(name[:3])
print('')

#3.21
#Print only even numbers in a list
numList = [2, 3, 4, 5, 6, 7, 8, 9]
for number in numList:
    if number % 2 == 0:
        print(number)
print('')

#3.22
#Print only if the square of a num is divisible by 8
for number in numList:
    if number**2 % 8 == 0:
        print(number)
print('')

#3.23
#Write for loops that use 'range()' and print the following sequences

#a) 0 1
for i in range(2):
    print(i)
print('')

#b) 0
for i in range(1):
    print(i)
print('')

#c) 3 4 5 6
for i in range(3, 7):
    print(i)
print('')

#d) 1
for i in range(1, 2):
    print(i)
print('')

#e) 0 3
for i in range(0, 4, 3):
    print(i)
print('')

#f) 5 9 13 17 21
for i in range(5, 22, 4):
    print(i)

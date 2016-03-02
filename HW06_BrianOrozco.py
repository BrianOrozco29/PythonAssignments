'''
Brian Orozco
September 27th, 2015
CS 100 - H01

Homework 06
'''

#Question 6
def check(aList):
    for element in range(len(aList)):
        if str(aList[element]) == aList[element+1]:
            return True
    return False
arg = [0, '0', 1, '1']
matched = check(arg)
print(matched)


'''
My answer is a. True
Correct answer: a.
'''

#Question 7
muchSnow = False
veryCold = True
takeTrain = True

if muchSnow:
    print("school closed")
else:
    print("give exam")
    
if veryCold:
    print("car won't start")
elif takeTrain:
    print("take exam")
else:
    print("miss exam")


'''
My answer is e. None of the above
Correct answer: e.
'''

#Question 8
isaac = ['I','do','not','fear','computers','I','fear','the','lack','of','them']
short = 3
shortCount = 0

for word in isaac:
    if len(word) <= short:
        shortCount += 1
        
print(shortCount)

'''
My answer is d. 6
Correct answer: d.
'''

#Question 9
def notIn(letter, wordList):
    rtnList = []
    for word in wordList:
        if letter not in word:
            rtnList.append(word)
    return rtnList

quote = ['round', 'up', 'the', 'usual', 'suspects']
print(notIn('e', quote))

'''
My answer is b. ['round', 'up', 'usual']
Correct answer: b.
'''

#Question 10
def accumulate(sequence):
    returnVal = []
    for element in sequence:
        returnVal.append(element)

    return returnVal

print(accumulate('anagram'))


'''
My answer is d.
Correct answer: d.
'''

"""
Question 12 (20 points)
Write a function named beginsWith() that computes how many strings in a list of strings begin with
a specified letter.
The function beginsWith() takes two parameters:
1. letter, a string of length 1
2. strList, a list of 0 or more strings
The function beginsWith() should return an integer that is the number of strings in strList that begin
with letter.
You may assume that no word in strList begins with a capital letter.
The following is an example of correct input and output for the function beginsWith():
>>> eliza = ['the','rain','in','spain','falls','mainly','on','the','plain']
>>> firstLetter = 't'
>>> print(beginsWith(firstLetter, eliza))
2

Question 13
Write a function named greeting(). The function greeting() should ask the user for their name, and then
ask the user for the day of the week. It should then greet the person by name and day and comment whether
their name has fewer, more than or the same number of characters as the day.
The function greeting() takes one parameter: a string named greetStr.
The following is an example of correct input and output for the function greeting():
>>> greeting('Happy')
What's your name? Justin
What day is today? Monday
Happy Monday Justin
Your name has the same number of characters as today!
"""

#Question 12

def beginWith(letter, strList):         #function takes a letter and a list
    count = 0
    for word in range(len(strList)):        #iterates for the length of given list
        if strList[word][:1] == letter:         #checks if 1st char is equal to given letter
            count += 1                              #if so, adds 1 to count variable
    return count                            #gives back value of count variable

list1 = ['banana', 'bat', 'hood', 'in', 'smart', 'basketball', 'salad']
firstLetter = 'b'
print(beginWith(firstLetter, list1))

#Question 13

def greeting(greetStr):
    name = input('What is your name? ')     #asks for name and sets it to variable name
    day = input('What day is today? ')      #asks for the day and sets it to variable day
    print(greetStr + ' ' + day + ' ' + name)    #prints greeting using parameter, name, and day variables

    if len(name) == len(day):               #if-else statements compare word length and day length
        print('Your name has the same number of characters as today!')

    elif len(name) <= len(day):
        print('Your name has a smaller number of characters as today!')

    elif len(name) >= len(day):
        print('Your name has more characters than that of today!')

    else:
        print('User input error, try again')

greeting('Happy')
    

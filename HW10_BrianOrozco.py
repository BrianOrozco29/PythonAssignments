'''
Brian Orozco
October 12th, 2015
CS 100 - H01

Homework 10
'''

"""
Problem 1.
This problem provides practice using a while True loop.
 
Write a function named twoWords that gets and returns two words from a user. The first word is of a specified length, and the second word begins with a specified letter.

The function twoWords takes two parameters:

i.	an integer, length, that is the length of the first word and
ii.	a character, firstLetter, that is the first letter of the second word. The second word may begin with either an upper or lower case instance of firstLetter.

The function twoWords should return the two words in a list.

Use a while True loop and a break statement in the implementation of twoWords.

The following is an example of the execution of twoWords:

print(twoWords(4, 'B'))
A 4-letter word please two
A 4-letter word please one
A 4-letter word please four
A word beginning with B please apple
A word beginning with B please pear
A word beginning with B please banana
['four', 'banana']

Problem 2.
Write a function named twoWordsV2 that has the same specification as Problem 1, but implement it using while and not using break. (Hint: provide a different boolean condition for while.)

Since only the implementation has changed, and not the specification, for a given input the output should be identical to the output in Problem 1.

Problem 3.
Do problem 5.29 in the textbook. (This problem is the same in editions 1 and 2.)

Problem 4.
Do problem 5.33 in the textbook. (This problem is the same in editions 1 and 2.)

Problem 5.
Write a function named enterNewPassword. This function takes no parameters. It prompts the user to enter a password until the entered password has 8-15 characters, including at least one digit. Tell the user whenever a password fails one or both of these tests.
"""

#Problem 1
def twoWords(length, firstLetter):  
    while True:
        numWord = input("Enter a " + str(length) + " letter word: ")
        if len(numWord) == length:
             break
        else:
            continue
    while True:
        firstLetterWord = input("Enter a word that starts with " + firstLetter + ": ")
        if firstLetterWord[0] == firstLetter:
            break
        else:
            continue

    wordList = [numWord, firstLetterWord]
    return wordList

print(twoWords(5, "B"))

print("")

#Problem 2
def twoWordsV2(length, firstLetter):  
    while True:
        numWord = input("Enter a " + str(length) + " letter word: ")
        if len(numWord) != length:
            continue
    while True:
        firstLetterWord = input("Enter a word that starts with " + firstLetter + ": ")
        if firstLetterWord[0] != firstLetter:
            continue

    wordList = [numWord, firstLetterWord]
    return wordList

print(twoWords(3, "D"))

print("")

#Problem 3
def lastfirst(nameList):
    firstList = []
    lastList = []
    for i in nameList:
        a = i.split(', ')
        lastList.append(a[0])
        firstList.append(a[1]) 

    list2 = [firstList, lastList]
    return print(list2)

list1 = ['Orozco, Brian', 'Chan, Jackie', 'Cena, John']
lastfirst(list1)

print("")

#Problem 4
def mystery(n):
    count = 0
    while n != 1:
        n = n // 2
        count += 1        
    return print(count)

mystery(25)

print("")

#Problem 5
def enterNewPassword():
    password = ""
    def stringContainsADigit(n):
        for i in n:
            if i in "0123456789":
                return True
        return False
    
    while True:
        password =  input("Enter a password: " )
        print("")
        if len(password) > 15 or len(password) < 8:
            print("Your password must contain at least 8 characters (including at least one digit), but no more than 15! Try Again.")
            continue
        if stringContainsADigit(password):
                break
        else:
                print("Your password must contain at least 1 digit! Try Again")
                continue
    print("Congratulations, you have made a password!")
    return password
        
enterNewPassword()
    

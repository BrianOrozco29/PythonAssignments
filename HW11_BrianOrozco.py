'''
Brian Orozco
October 12th, 2015
CS 100 - H01

Homework 11
'''
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
    

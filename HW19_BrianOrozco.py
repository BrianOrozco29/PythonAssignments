'''
Brian Orozco
CS 100 H01
Homework 19

Novemver 23, 2015
'''

#Question 1
def fifthOneOdd(numlist):
    for i in range(0, len(numlist)):
        if i%5 != 0:
            continue
        if numlist[i]%2 != 1:
            return False
    return True
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(fifthOneOdd(nums))

'''
My answer is b. False
Correct answer: b.
'''

#Question 2
def hasVowel(wordList):
    vowels = 'aeiouAEIOU'
    rtnList = []
    for word in wordList:
        for letter in word:
            if letter in vowels:
                rtnList.append(word)
                break
    return rtnList
subwayAd = ['Rd', 'ths', 'to', 'gt', 'a', 'gd', 'jb']
print(hasVowel(subwayAd))

'''
My answer is c. ['to','a']
Correct answer: c.
'''

#Question 3
aString = 'Springsteen, Springsteen, oh, Springsteen!'
aList = aString.split()
bossCount = 0
for word in aList:
    if word == 'Springsteen':
        bossCount += 1
print(bossCount)

'''
My answer is a. 0
Correct answer a.
'''

#Question 4
titles = ['Ulysses', 'Typhoon', 'Eeyore', 'Brigadoon', 'Oo! Ah! Ee!']
double = []
for title in titles:
    for i in range(len(title)-1):
        if title[i] == title[i+1]:
            double.append(title)
print(double)

'''
My answer is c. ['Ulysses', 'Typhoon', 'Brigadoon']
Correct answer c.
'''

#Question 5
def vowelTest(testStr):
    vowels = 'aeiou'
    vowelsInTestStr = ''
    for letter in testStr:
        if letter in vowels:
            vowelsInTestStr += letter
    return vowelsInTestStr
t = 'you heard it here'
print(vowelTest(t))

'''
My answer is b. oueaiee
Correct answer: b.
'''

#Question 11a
import turtle
def tri(t, size):
    for i in range(3):
        t.down()
        t.fd(size)
        t.left(120)

#Question 11b
def trifecta(size, angle, num):
    t = turtle.Turtle()
    for i in range(num):
        tri(t, size)
        t.right(angle)

  

#Question 12
def makeWordList(readFileName, writeFileName):
    inF = open(readFileName, 'r')
    outF = open(writeFileName, 'w')

    content = inF.read()
    wordList = content.split()
    for word in wordList:
        count = 0
        count += wordList.count(word)
        outF.write(word + ' ' + str(count) + '\n')

    inF.close()
    outF.close()
    return outF

makeWordList('testFile.txt', 'outfile.txt')
    


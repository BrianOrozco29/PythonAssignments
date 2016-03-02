'''
Brian Orozco
November 9th, 2015
CS 100 H01

Homework 17
Do even-numberred problems
'''
#Question 0 (My group)
import turtle
t = turtle.Turtle()
s = turtle.Screen()

def snowflake(t, legLength):
    for i in range(6):
        t.fd(legLength)
        t.circle(1)
        t.bk(legLength)
        t.left(60)

def snowflakes(t, length, angle, incr, numFlakes):
    for i in range(numFlakes):
        snowflake(t, length)
        t.penup()
        t.fd(length*2)
        t.pendown()
        t.left(angle)
        length += incr



#Question 2
import string
def countPunc(inFile):
    inF = open(inFile)
    puncDict = {}
    content = inF.read()
    
    for i in content:
        if i not in string.punctuation:
            continue

        if i not in puncDict:
            puncDict[i] = 1         
        elif i in string.punctuation:
            puncDict[i] += 1

            
    inF.close()
    return puncDict


    
#Question 4
hc = open("Hotel California.txt")
bth = open("Breaking The Habit.txt")
aa = open("Alphabet Aerobics.txt")
ww = open("Wonderwall.txt")
wa = open("Walk.txt")
lyrDict = {"Hotel California": hc.read(), "Breaking The Habit": bth.read(), "Alphabet Aerobics": aa.read(), "Wonderwall": ww.read(), "Walk": wa.read()}
hc.close()
bth.close()
aa.close()
ww.close()
wa.close()


def lyricCount(lyrics, lyric, outfile):   
    result = ""
    
    for key in lyrics:
        count = 0
        count += lyrics[key].count(lyric)
        outF.write("'" + lyric + "'" + " appears: " + str(count) + " time(s) in the song: " + key + "\n")
    
    return outF

outF = open('outfile.txt', 'w')
lyricCount(lyrDict, "the", outF)
outF.close()

#Question 6
def drawAxis(t, xaxis, yaxis):
    t.fd(xaxis/2)
    t.bk(xaxis)
    t.fd(xaxis/2)
    t.left(90)
    t.fd(yaxis/2)
    t.bk(yaxis)
    t.fd(yaxis/2)
    t.right(90)

def drawGridLines(t, xaxis, yaxis, numTicksx, numTicksy):
    drawAxis(t, xaxis, yaxis)
    t.bk(xaxis/2)

    for i in range(int(numTicksx + 1)):
        t.down()
        t.left(90)
        t.fd(xaxis/20)
        t.bk(xaxis/10)
        t.fd(xaxis/20)
        t.right(90)
        t.up()
        t.fd(xaxis/10)

    t.bk((xaxis/10) * 6)
    t.left(90)
    t.bk(yaxis/2)
    for i in range(int(numTicksy + 1)):
        t.down()
        t.left(90)
        t.fd(yaxis/20)
        t.bk(yaxis/10)
        t.fd(yaxis/20)
        t.right(90)
        t.up()
        t.fd(yaxis/10)


#Question 8
def beginsWith(txt, letter):
    letterDict = {}
    list1 = txt.split()
    for i in list1:
        if letter in i: 
            letterDict[i] = txt.count(i)
    return letterDict

txt = 'hopefully this works and gives me no problems whatsoever or else I will be really upset'
print(beginsWith(txt, 'w'))

    

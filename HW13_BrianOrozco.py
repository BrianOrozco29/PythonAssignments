'''
Brian Orozco
October 8th, 2015
CS 100 - H01

2nd AI Bagels Problem HW13
'''

'''
In my code, the computer takes a guess (starting at 100) and randomly generated number, and separates them into lists,
If a digit yields bagels, then 1 unit will be added to that digit until it equals the digit of the actual number.
Finally, the code will add up every time 1 unit was added to any digit.
'''


import random
def bagels():
    

    guess = 100
    count = 0
    num = int(random.randint(100, 999)) #takes a num from 100 to 1000
    
    digitList = []    
    digitList.append(int(num / 100))        
    digitList.append(int((num % 100)/10))   
    digitList.append(num % 10)

    guessList = []  
    guessList.append(int(guess / 100))     
    guessList.append(int((guess % 100)/10)) 
    guessList.append(guess % 10)            
            

    while True: 

        if digitList != guessList:  
            while True:
                if digitList[0] != guessList[0]:   
                    guessList[0] += 1
                    count += 1
                    print(str(count) + " guesses!")
                        
                else:  
                    break

            while True:
                if digitList[1] != guessList[1]:   
                    guessList[1] += 1
                    count += 1
                    print(str(count) + " guesses!")
                else:
                    break

            while True:
                if digitList[2] != guessList[2]:    
                    guessList[2] += 1
                    count += 1
                    print(str(count) + " guesses!")
                else:
                    break
        else:
            return count
        
       

                 

print(str(bagels()) + " total guesses")




    

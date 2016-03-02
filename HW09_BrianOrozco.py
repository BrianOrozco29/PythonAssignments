'''
Brian Orozco
October 8th, 2015
CS 100 - H01

2-Player Bagels Problem HW09
'''

import random
def bagels():
    '''
    This part of the function is just to setup the situation by randomly
    generating the actual number, and declaring the guess variable as a place holder.
    '''
    
    print('Welcome to BAGELS: VS. EDITION!!! Here are the rules.')
    print('First, player 1 guesses a whole number between 100 and 1000!')
    print('Then use the clues to find out how close you are to the actual number. After that, player 2 tries to guess the number. \nKeep Guessing until one of you gets it! \n     "Bagels" means one of the digits in your guess is not present in the number. \n     "Picos" means one of your digits IS present, but is not in the right position. \n     "Fermis" means your digit is both the number AND in the correct position.')
    print('Have Fun!!!')

    guess = 0
    num = int(random.randint(100, 1000)) #takes a num from 100 to 1000
    
    digitList = []  #attempt to separate digits of random #   
    digitList.append(int(num / 100))        #takes 1st digit of random # and puts into dL
    digitList.append(int((num % 100)/10))   #takes 2nd digit of random # to dL
    digitList.append(num % 10)              #takes 3rd digit of random # to dL


    player1 = True     #Sets up booleans for each player, to decide who goes when
    player2 = False



    while guess != num: #loop that ensures the user will have as many attempts to guess as needed
        if player1:
            guess = int(input("What's your guess, Player 1?\n")) #user takes a guess
            
            print("")
            
            guessList = []  #attempt to separate digits of the guess
            guessList.append(int(guess / 100))      #takes 1st digit of random # and puts into gL
            guessList.append(int((guess % 100)/10)) #takes 2nd digit of random # to gL
            guessList.append(guess % 10)            #takes 3rd digit of random # to gL
            
            bagel = 0   #Sets up and re-assigns clue variables
            picos = 0
            fermis = 0

            if digitList != guessList:  #First checks the entire set of digits of both numbers
                if digitList[0] != guessList[0]:    #Compares 1st digit of both numbers
                    if guessList[0] == digitList[1] or guessList[0] == digitList[2]:    #Checks if first digit is either bagels or picos
                        picos += 1
                    else:
                        bagel += 1
                else:   #If they are identical digits in the same position, then it is a fermis
                    fermis += 1

                if digitList[1] != guessList[1]:    #Compares 2nd digits
                    if guessList[1] == digitList[2] or guessList[1] == digitList[0]:    #Checks if bagels or picos
                        picos += 1
                    else:
                        bagel += 1
                else:
                    fermis += 1

                if digitList[2] != guessList[2]:    #Compares the final digits
                    if guessList[2] == digitList[0] or guessList[2] == digitList[1]:
                        picos += 1
                    else:
                        bagel += 1
                else:
                    fermis += 1
            else:
                fermis = 3
                
            #This next line gives the user the results of their guess        
            print('Bagels: ' + str(bagel) + '\nPicos: ' + str(picos)+ '\nFermis: ' + str(fermis) + '\n')
            

            #These lines react to the amount of each clue word, in order to encourage the user to keep playing
            if bagel == 3:
                print("Not even close...\nTry Again!")
            elif bagel == 2:
                print("Getting closer...\nOnce More!")
            elif bagel == 1:
                if fermis == 2:
                    print("It's so close you can almost taste the bagels! \nKeep Going!")
                else:
                    print("Not too far now! \nKeep at it!")
            else:
                if picos == 3:
                    print("So close...yet so far. \nAgain!")
                elif picos == 2 and fermis == 1:
                    print("You've almost got it!!!! \nFINISH IT!!!")

            player1 = False
            player2 = True

        elif player2:
            
                guess = int(input("What's your guess, Player 2?\n")) #user takes a guess     

                print("")
                
                guessList = []  #attempt to separate digits of the guess
                guessList.append(int(guess / 100))      #takes 1st digit of random # and puts into gL
                guessList.append(int((guess % 100)/10)) #takes 2nd digit of random # to gL
                guessList.append(guess % 10)            #takes 3rd digit of random # to gL
                
                bagel = 0   #Sets up and re-assigns clue variables
                picos = 0
                fermis = 0

                if digitList != guessList:  #First checks the entire set of digits of both numbers
                    if digitList[0] != guessList[0]:    #Compares 1st digit of both numbers
                        if guessList[0] == digitList[1] or guessList[0] == digitList[2]:    #Checks if first digit is either bagels or picos
                            picos += 1
                        else:
                            bagel += 1
                    else:   #If they are identical digits in the same position, then it is a fermis
                        fermis += 1

                    if digitList[1] != guessList[1]:    #Compares 2nd digits
                        if guessList[1] == digitList[2] or guessList[1] == digitList[0]:    #Checks if bagels or picos
                            picos += 1
                        else:
                            bagel += 1
                    else:
                        fermis += 1

                    if digitList[2] != guessList[2]:    #Compares the final digits
                        if guessList[2] == digitList[0] or guessList[2] == digitList[1]:
                            picos += 1
                        else:
                            bagel += 1
                    else:
                        fermis += 1
                else:
                    fermis = 3
                    
                #This next line gives the user the results of their guess        
                print('Bagels: ' + str(bagel) + '\nPicos: ' + str(picos)+ '\nFermis: ' + str(fermis) + '\n')
                

                #These lines react to the amount of each clue word, in order to encourage the user to keep playing
                if bagel == 3:
                    print("Not even close...\nTry Again!")
                elif bagel == 2:
                    print("Getting closer...\nOnce More!")
                elif bagel == 1:
                    if fermis == 2:
                        print("It's so close you can almost taste the bagels! \nKeep Going!")
                    else:
                        print("Not too far now! \nKeep at it!")
                else:
                    if picos == 3:
                        print("So close...yet so far. \nAgain!")
                    elif picos == 2 and fermis == 1:
                        print("You've almost got it!!!! \nFINISH IT!!!")

                player1 = True
                player2 = False

    if player2:
        print("Player 1 wins! Congratulations!")
    else:
        print("Player 2 wins! Congratulations!")
        

                 

bagels()


    

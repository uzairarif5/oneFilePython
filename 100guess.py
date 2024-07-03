'''
Challenge the computer with this sum game to reach 100 first
'''

import time
import random

def playagain():
    again = input("Do you want to play again?\n")
    def innerfunc():
        nonlocal again
        if again == 'yes':
            print('\n')
            options()
        elif again == "no":
            print("bye")
        else:
            print("Please type just 'yes' or 'no'...")
            again = input()
            innerfunc()
    innerfunc()

def inputnum():
    print('input a number from 1 to 10')
    number = 0
    def checkinput():
        nonlocal number
        number = input()
        try:
            number = int(number)
            if (number < 1) or (number > 10):
                print('please input between 1 and 10 only')
                checkinput()
        except:
            print('please input between 1 and 10 only')
            checkinput()
    checkinput()
    return number

def selectnum(num, prevsum, impossible):
    doTrick = False
    specialArray = [34,45,56,67,78,89]
    for specialNum in specialArray:
        if prevsum == specialNum:
            doTrick = True
    if (doTrick == True) or (impossible == True):
        return (11 - num)
    else:
        currentsum = num + prevsum
        if (currentsum > 78) and (currentsum < 89):
            return (89 - currentsum)
        elif (currentsum > 67) and (currentsum < 78):
            return (78 - currentsum)
        elif (currentsum > 89):
            return (100 - currentsum)
        else:
            if (currentsum > 56) and (currentsum <= 67):
                return random.randint(1,3)
            else:
                return random.randint(1,10)

def playgame(playernum, compnum, thesum, gamemode):
    impossible = False #(makes gamemode 1 impossible) can only be changed by the programmer, and not by the user
    if gamemode == 2:
        impossible = False
        compnum = random.randint(1,10)
        thesum = playernum + compnum + thesum
        print("Comp chooses " + str(compnum))
    print("\n----------------------------------------------------------\nYour Number:\tComp Number:\tTotal Sum:")
    print(str(playernum) + "\t\t" + str(compnum) + "\t\t" + str(thesum) + "\n---------------------------------------------------------\n")
    Lost = True
    while (thesum < 100):
        prevsum = thesum
        playernum = inputnum()
        thesum = playernum + thesum
        if (thesum > 99):
            Lost = False
        compnum = selectnum(playernum, prevsum, impossible)
        thesum = compnum + thesum
        print("Comp chooses " + str(compnum))
        print("\n-----------------------------------------------------\nYour Number:\tComp Number:\tTotal Sum:")
        print(str(playernum) + "\t\t" + str(compnum) + "\t\t" + str(thesum) + "\n-----------------------------------------------------\n")
    if Lost == False:
        print('You won!\nYou got to a hundred first!\n')
    else:
        print('Comp has won the game!\n')
    time.sleep(3)
    playagain()

def gamemode():
    gm = input('\nType 1 if you want the computer to make the first move, otherwise type 2:\n')
    while (gm != '1') and (gm != '2'):
        gm = input("Please type 1 or 2 (no spaces):\n")
    if gm == '1':
        print('\nComp chooses 1')
        playgame(0, 1, 1, 1)
    else:
        print("")
        first = inputnum()
        playgame(first, 0, 0, 2)

def options():
    op = input('Type 1 to play the game\nType 2 to learn how to play\n')
    def checkinput(choice):
        if choice == '1':
            gamemode()
        elif choice == '2':
            print('You and the computer will take turns choosing a number and that number will be added to the total sum, the first one to make the sum above 99 wins the game.\n')
            time.sleep(5)
            options()
        else:
            retry = input('please type 1 or 2 only\n')
            checkinput(retry)
    checkinput(op)
options()

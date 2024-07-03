'''
Can you guess the number before the timer runs out!
'''

from time import *
from random import *

print('\n\nWelcome Toooooo "Guess The Secret Number"')
print (r'type "1" for easy (1-10) (5 seconds)')
print (r'type "2" for medium (1-100) (10 seconds)')
print (r'type "3" for hard (1-1000) (20 seconds)')
mode = (input('>>>'))
def check():
    global mode
    global l
    global t
    if mode != '1':
        if mode == '2':
            l = 100
            t = 10
        elif mode =='3':
            l = 1000
            t = 20
        else:
            print('Plz type 1, 2 or 3')
            mode = (input('>>>'))
            return check()
    else:
        l = 10
        t = 5
check()
i = randint(1,l)
print('----------')
print('The timer has started!!!\n')
start = time()
def num():
    try:
        global no
        no = int(input('Guess the secret number: '))
    except ValueError:
        print('Plz Type A Number\n')
        sleep (1)
        return num()
    e = time()
    d2 = round(e - start)
    if d2 > t:
        print('\n----------')
        print ('You lose... you took longer than', t ,'seconds and the secret number was', i, end='')
        print ('.\nBetter luck next time')
    else:
        if i > no:
            print ('\n' + 'Secret number is bigger')
            return num()
        elif i < no:
            print ('\n' + 'Secret number is smaller')
            return num()
        else:
            a = str(i)
            end1 = time()
            d = round(end1 - start)
            print ('\nYou guessed it right, the secret number is ' + a)
            sleep(1)
            print ('You took ', d, ' seconds')
num()

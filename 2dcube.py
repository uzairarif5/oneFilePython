'''
It\'s like a Rubik\'s Cube... but 2d.
Your minimum score is stored in the `2dminscore.txt` file
'''

from tkinter import *
from random import *
import tkinter.messagebox as box
from time import *
import math

#start
winbf = Tk()
winbf.title('2dCube!!!')
winbf.resizable(0,0)
win = Frame(winbf)
win.grid()
win.configure(bg='gray')
win.grid_forget()
menu = Frame(winbf)
menu.grid()
menu.configure(bg='gray')

#change num
def changenum(Btype, fromChangeFunc = "no"):
    global starttimer
    if Btype == 't1':
        temp = num1.cget('text')
        num1.configure(text=num4.cget('text'))
        num4.configure(text=num7.cget('text'))
        num7.configure(text=temp)
    if Btype == 't2':
        temp = num2.cget('text')
        num2.configure(text=num5.cget('text'))
        num5.configure(text=num8.cget('text'))
        num8.configure(text=temp)
    if Btype == 't3':
        temp = num3.cget('text')
        num3.configure(text=num6.cget('text'))
        num6.configure(text=num9.cget('text'))
        num9.configure(text=temp)
    if Btype == 'r1':
        temp = num1.cget('text')
        num1.configure(text=num2.cget('text'))
        num2.configure(text=num3.cget('text'))
        num3.configure(text=temp)
    if Btype == 'r2':
        temp = num4.cget('text')
        num4.configure(text=num5.cget('text'))
        num5.configure(text=num6.cget('text'))
        num6.configure(text=temp)
    if Btype == 'r3':
        temp = num7.cget('text')
        num7.configure(text=num8.cget('text'))
        num8.configure(text=num9.cget('text'))
        num9.configure(text=temp)
    if Btype == 'd1':
        temp = num1.cget('text')
        num1.configure(text=num7.cget('text'))
        num7.configure(text=num4.cget('text'))
        num4.configure(text=temp)
    if Btype == 'd2':
        temp = num2.cget('text')
        num2.configure(text=num8.cget('text'))
        num8.configure(text=num5.cget('text'))
        num5.configure(text=temp)
    if Btype == 'd3':
        temp = num3.cget('text')
        num3.configure(text=num9.cget('text'))
        num9.configure(text=num6.cget('text'))
        num6.configure(text=temp)
    if Btype == 'l1':
        temp = num3.cget('text')
        num3.configure(text=num2.cget('text'))
        num2.configure(text=num1.cget('text'))
        num1.configure(text=temp)
    if Btype == 'l2':
        temp = num6.cget('text')
        num6.configure(text=num5.cget('text'))
        num5.configure(text=num4.cget('text'))
        num4.configure(text=temp)
    if Btype == 'l3':
        temp = num9.cget('text')
        num9.configure(text=num8.cget('text'))
        num8.configure(text=num7.cget('text'))
        num7.configure(text=temp)
    if (['1','2','3','4','5','6','7','8','9'] == [num1.cget('text'),num2.cget('text'),num3.cget('text'),num4.cget('text'),num5.cget('text'),num6.cget('text'),num7.cget('text'),num8.cget('text'),num9.cget('text')] and fromChangeFunc == "no"):
        finishtimer = time()
        totaltime = int(finishtimer - starttimer)
        if totaltime < score:
            minimum = totaltime
            file = open('2dminscore.txt','w')
            file.write(str(totaltime))
            file.close()
        else:
            minimum = score
        box.showinfo('You won','Wow you atually did it.\n\nYou took ' + str(totaltime) + ' seconds.\nMinimum time: ' + str(minimum))
        menu.grid()
        win.grid_forget()
    
#change
def change():
    arrowlist = ['t1','t2','t3','r1','r2','r3','d1','d2','d3','l1','l2','l3']
    for i in range(2):
        index = randint(0,11)
        changenum(arrowlist[index], "yes")
        if ['1','2','3','4','5','6','7','8','9'] == [num1.cget('text'),num2.cget('text'),num3.cget('text'),num4.cget('text'),num5.cget('text'),num6.cget('text'),num7.cget('text'),num8.cget('text'),num9.cget('text')]:
            change()

#start
def start():
    global starttimer
    global score
    menu.grid_forget()
    win.grid()
    try:
        file = open('2dminscore.txt','r')
        score = int(file.read())
        file.close()
    except:
        score = math.inf
    change()
    starttimer = time()
title = Label(menu,text='2dCube!!!',width='50',height='8',relief='groove')
title.grid(row=1,column=1,pady=('80','0'),columnspan=2)
startB = Button(menu,text='START',command=start,height='5',width='30')
startB.grid(padx=('100','50'),pady='100',row=2,column=1)
quitB = Button(menu,text='QUIT',command=exit,height='5',width='30')
quitB.grid(padx=('50','100'),pady='100',row=2,column=2)

#numbers
num1 = Label(win,text='3',width=2,relief='solid')
num1.grid(row=2,column=2)
num2 = Label(win,text='1',width=2,relief='solid')
num2.grid(row=2,column=3)
num3 = Label(win,text='2',width=2,relief='solid')
num3.grid(row=2,column=4)
num4 = Label(win,text='4',width=2,relief='solid')
num4.grid(row=3,column=2)
num5 = Label(win,text='5',width=2,relief='solid')
num5.grid(row=3,column=3,pady='10',padx='10')
num6 = Label(win,text='6',width=2,relief='solid')
num6.grid(row=3,column=4)
num7 = Label(win,text='7',width=2,relief='solid')
num7.grid(row=4,column=2)
num8 = Label(win,text='8',width=2,relief='solid')
num8.grid(row=4,column=3)
num9 = Label(win,text='9',width=2,relief='solid')
num9.grid(row=4,column=4)

#arrows
arrowt1 = Button(win,text='^',width=2,command = lambda: changenum('t1'))
arrowt1.grid(row=1,column=2,pady='20')
arrowt2 = Button(win,text='^',width=2,command = lambda: changenum('t2'))
arrowt2.grid(row=1,column=3,pady='20')
arrowt3 = Button(win,text='^',width=2,command = lambda: changenum('t3'))
arrowt3.grid(row=1,column=4,pady='20')
arrowr1 = Button(win,text='<',width=2,command = lambda: changenum('r1'))
arrowr1.grid(row=2,column=1,padx='20')
arrowr2 = Button(win,text='<',width=2,command = lambda: changenum('r2'))
arrowr2.grid(row=3,column=1,padx='20')
arrowr3 = Button(win,text='<',width=2,command = lambda: changenum('r3'))
arrowr3.grid(row=4,column=1,padx='20')
arrowd1 = Button(win,text='V',width=2,command = lambda: changenum('d1'))
arrowd1.grid(row=5,column=2,pady='20')
arrowd2 = Button(win,text='V',width=2,command = lambda: changenum('d2'))
arrowd2.grid(row=5,column=3,pady='20')
arrowd3 = Button(win,text='V',width=2,command = lambda: changenum('d3'))
arrowd3.grid(row=5,column=4,pady='20')
arrowl1 = Button(win,text='>',width=2,command = lambda: changenum('l1'))
arrowl1.grid(row=2,column=5,padx='20')
arrowl2 = Button(win,text='>',width=2,command = lambda: changenum('l2'))
arrowl2.grid(row=3,column=5,padx='20')
arrowl3 = Button(win,text='>',width=2,command = lambda: changenum('l3'))
arrowl3.grid(row=4,column=5,padx='20')

#mainloop
win.mainloop()

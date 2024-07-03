'''
A Tkinter project that lets you test Tkinter fonts.
'''

from tkinter import *
import tkinter.font

win = Tk()
win.resizable(0,0)
display = Frame(win)
display.grid(padx=10,pady=10)

def chosen():
    global first
    global default
    global fs
    if first == False:
        default = show.get(1.0,'end')
    else:
        first = False
    show.delete(1.0,'end')
    try:
        selection = listb.get(listb.curselection())
        show.configure(font=(selection,fs))
        show.insert('1.0', default)
    except:
        pass
    show.tag_add('center','1.0','end')

def incfs():
    global fs
    if int(fs) < 20:
        fs = str(int(fs)+1)
    number.configure(text=fs)

def decfs():
    global fs
    if int(fs) > 0:
        fs = str(int(fs)-1)
    number.configure(text=fs)
    
fs = '12'
listb = Listbox(display,height=30,width=35)
listb.grid(padx=10,row=1,column=1,rowspan=2)
cb = Button(display,text='Choose',command=chosen)
cb.grid(row=2,column=3)
number = Label(display,text=fs,relief='groove',width=5,height=3,bg='lavender')
number.grid(row=2,column=2,padx=('0','35'))
upb   = Button(display,text='+',width=2,height=1,bg='darkseagreen1',command=incfs)
upb.grid(row=2,column=2,padx=('35','0'),pady=('0','28'))
downb = Button(display,text='-',width=2,height=1,bg='light coral',command=decfs)
downb.grid(row=2,column=2,padx=('35','0'),pady=('26','0'))
counter = 1

for i in sorted(tkinter.font.families()):
    counter += 1
    listb.insert(counter,i)

show = Text(display,bg='white',relief='solid',width=40,height=11)
show.grid(row=1,column=2,columnspan=2,padx=10)
show.insert('1.0','  ')
show.tag_configure("center", justify='center')
show.tag_add('center','1.0','end')
default = '\n\nABCDEFGHIJKLMNOPQ\nRSTUVWXYZ\n\nabcdefghijklmnopq\nrstuvwxyz\n\n0123456789'
first = True

win.mainloop()

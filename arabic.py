'''
Made for learning Arabic verb conjugation.
How many can you get correct in 30 seconds?
'''

from tkinter import *
from random import *
import tkinter.messagebox as box
from time import *
import sys

winbf = Tk()
win = Frame(winbf)
win.pack()
win.configure(bg='gray90')
winbf.resizable('0','0')
winbf.title('Arabic')
title = Label(win,width=45,borderwidth=2, height=7, relief='solid' ,bg='light blue',text='Studying Present Tense In Arabic',font=('calibri','20','bold'), fg='white')

def makeList():
	global arabic
	global arabic2
	arabic = [
		'He studies',
		'They (m) (dual) study',
		'They (m) (pl) study',
		'She studies',
		'They (f) (dual) study',
		'They (f) (pl) study',
		'You (m) study',
		'You (m) (dual) study',
		'You (m) (pl) study',
		'You (f) study',
		'You (f) (dual) study',
		'You (f) (pl) study',
		'I study',
		'We study'
		]

	arabic2 = [
		'يَدْرُسُ',
		'يَدْرُسانِ',
		'يَدْرُسُونَ',
		'تَدْرُسُ',
		'تَدْرُسانِ',
		'يَدْرُسْنَ',
		'تَدْرُسُ',
		'تَدْرُسانِ',
		'تَدْرُسُونَ',
		'تَدْرُسِينَ',
		'تَدْرُسانِ',
		'تَدْرُسْنَ',
		'أَدْرُسُ',
		'نَدْرُسُ'
	]

def bexit():
	sys.exit()
	
def start():
	makeList()
	global display
	global num
	global score2b
	global score
	global stimer
	global game
	global win
	global check
	global correction
	global b1
	global b2
	global b3
	global b4
	global b5
	global b6
	global b7
	global b8
	global b9
	global b10
	global b11
	global b12
	global b13
	global b14
	global arabic2
	stimer = time()
	score = 0
	num= randint(0,13)
	word = arabic[num]
	win.pack_forget()
	game = Frame(winbf)
	game.grid()
	game.configure(bg='gray50')
	display = Label(game,width=45,borderwidth=2, height=7, text=word, font=("Courier", 15), relief='groove')
	display.grid(row=1,column = 1, columnspan =4, pady=('10','20'),padx='20')
	correction = Label(game,text=' ',relief='flat',font=('calibri','12'))
	correction.grid(row=1,column=1,columnspan=4,pady=('70','0'))
	quitb = Button(game,width=20,borderwidth=2, height=2, text='quit', font=("calibri", 15), relief='solid',command=bexit)
	quitb.grid(row=9,column = 3,columnspan=2, pady=('10','20'))
	score1b = Label(game,width=20,borderwidth=2, height=3, relief='solid', text=' score:', fg='SpringGreen2', bg ='slate gray',font=("fixedsys", 10, 'bold'), anchor='w')
	score1b.grid(row=9,column = 1,columnspan = 2, pady=('10','20'))
	score2b = Label(game,width=4,borderwidth=2, height=1, relief='flat', text=score, fg='alice blue', bg ='slate gray',font=("fixedsys", 10, 'bold'), anchor='e')
	score2b.grid(row=9,column = 1,columnspan = 2, pady=('10','20'))
	b1 = Button(game,relief='groove',font=('Calibri','15'),text = arabic2[0], command=lambda: bused(1))
	b2 = Button(game,relief='groove',font=('Calibri','15'),text = arabic2[1], command=lambda: bused(2))
	b3 = Button(game,relief='groove',font=('Calibri','15'),text = arabic2[2], command=lambda: bused(3))
	b4 = Button(game,relief='groove',font=('Calibri','15'),text = arabic2[3], command=lambda: bused(4))
	b5 = Button(game,relief='groove',font=('Calibri','15'),text = arabic2[4], command=lambda: bused(5))
	b6 = Button(game,relief='groove',font=('Calibri','15'),text = arabic2[5], command=lambda: bused(6))
	b7 = Button(game,relief='groove',font=('Calibri','15'),text = arabic2[6], command=lambda: bused(7))
	b8 = Button(game,relief='groove',font=('Calibri','15'),text = arabic2[7], command=lambda: bused(8))
	b9 = Button(game,relief='groove',font=('Calibri','15'),text = arabic2[8], command=lambda: bused(9))
	b10 = Button(game,relief='groove',font=('Calibri','15'),text = arabic2[9], command=lambda: bused(10))
	b11 = Button(game,relief='groove',font=('Calibri','15'),text = arabic2[10], command=lambda: bused(11))
	b12 = Button(game,relief='groove',font=('Calibri','15'),text = arabic2[11], command=lambda: bused(12))
	b13= Button(game,relief='groove',font=('Calibri','15'),text = arabic2[12], command=lambda: bused(13))
	b14= Button(game,relief='groove',font=('Calibri','15'),text = arabic2[13], command=lambda: bused(14))
	b1.grid(row = 2, column = 4,pady='5')
	b2.grid(row = 3,column = 4,pady='5')
	b3.grid(row = 4,column = 4,pady='5')
	b4.grid(row = 2,column = 3,pady='5')
	b5.grid(row = 3,column = 3,pady='5')
	b6.grid(row = 4,column = 3,pady='5')
	b7.grid(row = 2,column = 2,pady=('5'))
	b8.grid(row = 3,column = 2,pady='5')
	b9.grid(row = 4,column = 2,pady='5')
	b10.grid(row = 2,column = 1,pady='5')
	b11.grid(row = 3,column = 1,pady='5')
	b12.grid(row = 4,column = 1,pady='5')
	b13.grid(row = 5,column = 4,pady='15')
	b14.grid(row = 5,column = 3,pady='15')
	check = Label(game,borderwidth=2,width=2,height=1,relief='solid',text=' ',bg='khaki3')
	check.grid(row = 5, column = 1,columnspan=2)

def bused(ID):
	global num
	global display
	global score2b
	global score
	global stimer
	global game
	global win
	global check
	global correction
	global arabic2
	ftimer = time()
	x = ftimer - stimer
	if x >= 30:
		strscore = str(score)
		current = 0
		try:
			file = open ('arabic_score.txt','r')
			current = file.read()
			file.close()
		except:
			pass
		if int(current) < score:
			file = open ('arabic_score.txt','w')
			file.write(strscore)
			file.close()
			highest = score
		else:
			highest = current
		box.showinfo("Time's up", 'Your score is ' + strscore +'\nHighest score is ' + str(highest))
		game.grid_forget()
		win.pack()
	a = 0
	if (num+1) == ID:
		score += 1
		score2b.configure(text=score)
		check.configure(bg='forest green')
		game.after(500,changeback)
		a = 1
	else:
		if (ID == 5 or ID == 8 or ID == 11):
			if (num == 4 or num==7or num == 10):
				score += 1
				score2b.configure(text=score)
				check.configure(bg='forest green')
				game.after(500,changeback)
				a = 1
		if (ID == 4 or ID==7):
			if (num == 3 or num==6):
				score += 1
				score2b.configure(text=score)
				check.configure(bg='forest green')
				game.after(500,changeback)
				a = 1
		if a != 1:
			check.configure(bg='red3')
			answer = arabic2[num]
			correction.configure (text=answer)
			game.after(500,changeback)
			game.after(800,changeback2)
	b1.configure(state='disabled')
	b2.configure(state='disabled')
	b3.configure(state='disabled')
	b4.configure(state='disabled')
	b5.configure(state='disabled')
	b6.configure(state='disabled')
	b7.configure(state='disabled')
	b8.configure(state='disabled')
	b9.configure(state='disabled')
	b10.configure(state='disabled')
	b11.configure(state='disabled')
	b12.configure(state='disabled')
	b13.configure(state='disabled')
	b14.configure(state='disabled')

def changeback():
	global num
	check.configure(bg='khaki3')
	prenum = num
	num= randint(0,13)
	while num == prenum:
		num= randint(0,13)
	word = arabic[num]
	display.configure(text=word)
	b1.configure(state='normal')
	b2.configure(state='normal')
	b3.configure(state='normal')
	b4.configure(state='normal')
	b5.configure(state='normal')
	b6.configure(state='normal')
	b7.configure(state='normal')
	b8.configure(state='normal')
	b9.configure(state='normal')
	b10.configure(state='normal')
	b11.configure(state='normal')
	b12.configure(state='normal')
	b13.configure(state='normal')
	b14.configure(state='normal')
	
def changeback2():
	correction.configure (text=' ')
	
qb = Button(win,relief='groove', text = 'Quit',height=4,width=18, command=bexit)
sb = Button(win,relief='groove', text = 'Start',height=4,width=18,command=start)
title.pack(pady=('10','0'),padx='20')
qb.pack(pady=('30','20'), side='left',padx=('100','0'))
sb.pack(pady=('30','20'),side='right',padx=('0','100'))
win.mainloop()

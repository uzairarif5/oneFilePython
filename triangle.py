'''
Nothing wrong with a triangle
(may contain illuminati)
'''


#Symbol Input
def first():
	global s
	s = input('Symbol:')
	if len (s) != 1:
		print ('\nOne Character Only!\n')
		return first ()
	else:
		pass
first ()

#Row Input
def inp():
	global l
	q = (input('Number Of Rows:'))
	try:
		l = int(q)
	except ValueError:
		print ('\nThis is not an integer!\n')
		return inp()
	if l >= 25:
		print ('\nRows have to be less than 25!\n')
		return inp()
	else:
		pass
	if l < 1:
		print ('\nDont Enter Zero\n')
		return inp ()
	else:
		pass
inp ()
print ('\n')

#Triangle
def tri (c, q=0):
	a =2
	for i in range (c-1,0,-1):
		if a == 2:
			print (' ' * (c-2), s)
			a += 2
			e = (c-1)/2
			l = 2
		else:
			if e == i:
				print ((' ' * i) + (s) + (' ' * (i-1)) + '@' + (' ' * (i-1) + s))
				q += 2
				a = 10
			else:
				print ((' ' * i) + (s) + (' ' * (q+1)) + s)
				q += 2
	print ( s * (q+3))

#Output
if l == 1:
	print ('Any Number Except One')
else:
	tri (l)
if l % 2 == 1 and  l !=1:
	ic = ('**illuminati confirmed** ')
	print ('\n', ic.center((l*2)-3))
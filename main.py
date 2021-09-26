from os import  rename,remove
no_of_student = open('no.txt','r+')
no = no_of_student.read()
no = int(no)

a = input('Read, Write, Change existing, Delete an Entry or Reset(choose 1 , 2 , 3, 4, 5):')

if a == '1':
		info = open('all.txt','r')
		for i in range(no):
			x = info.readline()
			y = list(x.split('  '))
			name = y[0]
			roll = y[1]
			marks = y[2]
			print(f'{name} = {roll} = {marks}',end='')
		info.close()
elif a == '2':
	info = open('all.txt','a+')
	name = input('Enter Name :')
	roll = input('Enter roll no :')
	marks = input('Enter marks :')
	info.write(f'{name}  {roll}  {marks}\n')
	info.close()
	print('Sucessfully wrote the data in the database')
	no+=1
	no_of_student = open('no.txt','w+')
	no_of_student.write(str(no))
	no_of_student.close()
if a == '3' :
		info = open('all.txt','r')
		replace = open('all2.txt','w+')
		a = input('Enter Name or Roll no. of student to Change credentials :')
		for i in range(no):
			x = info.readline()
			if a in x :
				n = input('Enter Name :')
				r = input('Enter Roll no. :')
				m = input('Enter Marks:')
				replace.write(f'{n}  {r}  {m}\n')
			else:
				replace.write(x)
		remove('all.txt')
		rename('all2.txt','all.txt')
				 
		print('Sucessfully changed the data')
		
if a == '4' :
		info = open('all.txt','r')
		replace = open('all3.txt','w+')
		a = input('Enter Name or Roll no. of student to remove:')
		for i in range(no):
			x = info.readline()
			if a in x :
				pass
			else:
				replace.write(x)
		info.close()
		remove('all.txt')
		rename('all3.txt','all.txt')
				
		print('Sucessfully deleted the required entry.')
		no -= 1
		no = str(no)
		no_of_student = open('no.txt','w+')
		no_of_student.write(no)
				
if a == '5':
	x = open('all.txt','w+')
	y = open('no.txt','w+')
	y.write('0')
	print('Database reseted sucessfully.')

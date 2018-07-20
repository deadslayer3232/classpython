a = int(input('enter a number'))
names =[]
for i in range(a):
	names.append(input('enter a name : '))
for i in names:
	print('welcome {}'.format(i))

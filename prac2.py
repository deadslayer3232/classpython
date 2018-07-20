n = input('enter a number :')
if(n.isdigit()):
	sum = 0
	for i in range (0,len(n)):
		sum+=int(n[i])
		print (n[i])
		print (sum)
else:
	print('I am asking for a number dumbass')


#write a code to find the first 10 fibonachi numbers
a = 1
b = 1
print(a)
print(b)
for i in range(1,10):
	temp=b
	b=a+b
	a=temp
	print(b)
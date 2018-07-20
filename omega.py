lst = [i for i in range (0,16)]
print(lst)

# odd = list(map(lambda i: i%2!=0,lst))
# print(odd)

odd = list(filter(lambda i: i%2!=0,lst))
print(odd)
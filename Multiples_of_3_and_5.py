#Multiples of 3 and 5
temp = 0
for x in range(1,1001):
	if (x%3 == 0) or (x%5 ==0):
		temp=temp+x
print(temp)

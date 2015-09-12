import random
a = []
for value in range (100):
	a.append(random.randint(0,1000))
def trade(x,y):
	x=a[i]
	y=a[i+1]
	if x > y:
		temp = a[i+1]
		a[i+1] = a[i]
		a[i] = temp
count= len(a)-1

while count > 0:
	for i in range (0, len(a)-1):
		trade(a[i],a[i+1])
	count -= 1
print a
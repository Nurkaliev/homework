#1
'''
a = 2**3
b = 3**2
if a>b:
	print(a)
if b>a:
	print(b)
'''
#2
'''
n = (int(input('')), int(input('')), int(input('')))
print('максимальное-', max(n))
print('минимальное-', min(n))
'''
#3
'''
a = 17391%17
b = 546%17
c = 934%17
if a<c and a<b:
	print(17391)
if b<c and b<a:
	print(546)
if c<a and c<b:
	print(934)
'''
#4x
'''
x = 13**2
if x<172:
	print(x**2)
if x>172:
	print(x)
'''
#5
'''
a = int(input(''))
if a%2==0:
	print('четное число')
if a%3==0:
	print('оно делится на 3 без остатков')
if a**2>1000:
	print('оно больше 1000')

'''
#6
'''
n = int(input(''))
if n >=0 and n <=21 or n >=57 and n <=100:
	print(n)
else:
	print('запрешено')
'''
#7
'''
if True:
	print('ura')
'''
#8
'''
a = int(input(''))
if a>0:
	if a<10000:
		if a==a:
			print('ura')
'''
#9
'''
a = 10//5
b = 10/5
if a==b:
	print(a+b)
'''
#10
'''
b = int(input('->'))
if b==b:
	print(b-(b**2))
'''
#11
'''
a = 10
b = 5
if a>0 and b>0:
	print('они положительные')
'''
#12
'''
a = 10
b = 5
if a>b:
	print(a+2)
elif b>a:
	print(b+2)
'''

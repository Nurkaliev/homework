
'''
#1
lang1 = 'Rust'
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
if lang1 in languages:
	print('this languages is in list')
'''
'''
#2
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
	print(i)
	if i=='php':
		break
'''
'''
#3
a=7
while True:
	b=a**2
	c=b**2
	d=c**2
	e=d**2
	print(e)
	break
'''
'''
#4
l = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
a={n+1:l[n] for n in range(len(l))}
print(a)
'''
'''
#5
a=[]
for i in range(1,11):
	a.append(i)
x=list(reversed(a[:-1]))
a=a+x
print(a)
'''
'''
#6
a=[]
n = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
a.append(n[::2])
print(a)
'''
'''
#7
a=[]
n = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
a.append(n[1:12:2])
print(a)
'''
'''
#8
i = int(input('Введите число:'))
if i>=100  and i<1000:
	print('число трёхзначное')
if i>0:
	print('число положительное')
if i%2==0:
	print(' число чётное')
if i%2==1:
	print('число не чётное')
if i%31==0:
	print('число делится на 31 без остатка')
if i%31==1:
	print('число делится на 31 c остатком')
if i>100 and i%17==0 or i>150 and i==13**2:
	print(i)
'''

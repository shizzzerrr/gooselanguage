#программа для создания словарей с ключами

import random

filename = input('Введите имя нового словаря : ')

key = ['Г', 'г', 'А', 'а']

dic = []

for a in key:
	for b in key:
		for c in key:
			for d in key:
				un = a+b+c+d
				dic.append(un)

for a in range(2000):
	b = random.randint(0, 255)
	c = random.randint(0, 255)
	dic[b], dic[c] = dic[c], dic[b]

dct = ''
for a in range(256):
	dct += dic[a]

file = open(filename, 'w')

file.write(dct)

file.close()

print('Новый словарь создан.')
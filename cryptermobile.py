#программа для крипта \ декрипта текста по заданному словарю

import os
import sys

keys = 'ААаАаГАагГГГГаггААггАГггГаГАГгааагГаГАгГГААаААааааААаггГгАгГГгАаАГГГгагАггггААГГааааАГгАгАаагааАгГГааААГаГагагаГгаАаАаАГгГаГГггагАГгГаААгАГГагАаГАГагаааГГаГгааГаГГгГАаГААаГгГааАааААгГГаГаГгАаГГГГгаАгаГААгаааАГГАааГгАаАААГАГгАгаГГгаГаГААгаггагАГАаАгАгАгАГгГАгАаАААГАААгаГГГгагааГгГААГгАаГаАГГаАгАГААААаГгггГААгаАгггГагагГГггААггггггаАагГааГгАаааАГаГгГггГгГГгаГгГаГгггГААаАагГАгаГГаГАггГааАгГГгааАГГГааГгГаАагааАГаГАагггГгГааГгаагааГГгГГАГгагааАаАГаААГГгГААГАгаАаААггГаААггГгАгАаааГГГагагГГГаГГГааггГгаАААаггаГаАгАаАГГгГАаааГАагАгааггаГгаагГгГГаААгААгАагГГГагАГагААаАггАгаААГаГааАаГГаАГгггАГАгААГгаагггаагаАаГгГггГААгГгаАГааГаАГАгаГАгГаааГАГАаагАААГагАААаААаАаггггААаГаААГГАагААагагггагГГГААГагАгГгААГАГАаАгГАГгггГАгГАгГгГаГаагАггггааГгггаГГАААгаагааагГАггАаГаАаГАГГАГаааггаГГггГгГААаААГагАгАгаГгГгаАааГГГГаГАГагаАаггАГАААгаГАГГгаггАгаагГгаГГАГАаГАааАГАГАгаааАГгаАГАГГАГАаГАААагАаГГГагаАгагАаагАааГггГГгГгАГгАггГаггАаАГГААгААгаАгГаАагАггаггАГааАгАГААаАггГгААаАаАГГАгГАгаААгААагАааагГгАГггаАгАГАгААГАгГагаГаГГгГГагГГГгАГгаАГаАг'

dist = []

a, b, c, d = 0, 1, 2, 3

for cycle in range(256):
	keyy = keys[a] + keys[b] + keys[c] + keys[d]
	dist.append(keyy)
	a += 4
	b += 4
	c += 4
	d += 4

def program():

	os.system("clear")
	
	def crypt(text):
		textreturn = ''
		length = len(text)
		for letter in range(length):
			if text[letter].isalpha():
				if text[letter] == 'a':
					textreturn += dist[0]
				if text[letter] == 'b':
					textreturn += dist[1]
				if text[letter] == 'c':
					textreturn += dist[2]
				if text[letter] == 'd':
					textreturn += dist[3]
				if text[letter] == 'e':
					textreturn += dist[4]
				if text[letter] == 'f':
					textreturn += dist[5]
				if text[letter] == 'g':
					textreturn += dist[6]
				if text[letter] == 'h':
					textreturn += dist[7]
				if text[letter] == 'i':
					textreturn += dist[8]
				if text[letter] == 'j':
					textreturn += dist[9]
				if text[letter] == 'k':
					textreturn += dist[10]
				if text[letter] == 'l':
					textreturn += dist[11]
				if text[letter] == 'm':
					textreturn += dist[12]
				if text[letter] == 'n':
					textreturn += dist[13]
				if text[letter] == 'o':
					textreturn += dist[14]
				if text[letter] == 'p':
					textreturn += dist[15]
				if text[letter] == 'q':
					textreturn += dist[16]
				if text[letter] == 'r':
					textreturn += dist[17]
				if text[letter] == 's':
					textreturn += dist[18]
				if text[letter] == 't':
					textreturn += dist[19]
				if text[letter] == 'u':
					textreturn += dist[20]
				if text[letter] == 'v':
					textreturn += dist[21]
				if text[letter] == 'w':
					textreturn += dist[22]
				if text[letter] == 'x':
					textreturn += dist[23]
				if text[letter] == 'y':
					textreturn += dist[24]
				if text[letter] == 'z':
					textreturn += dist[25]
				if text[letter] == 'A':
					textreturn += dist[26]
				if text[letter] == 'B':
					textreturn += dist[27]
				if text[letter] == 'C':
					textreturn += dist[28]
				if text[letter] == 'D':
					textreturn += dist[29]
				if text[letter] == 'E':
					textreturn += dist[30]
				if text[letter] == 'F':
					textreturn += dist[31]
				if text[letter] == 'G':
					textreturn += dist[32]
				if text[letter] == 'H':
					textreturn += dist[33]
				if text[letter] == 'I':
					textreturn += dist[34]
				if text[letter] == 'J':
					textreturn += dist[35]
				if text[letter] == 'K':
					textreturn += dist[36]
				if text[letter] == 'L':
					textreturn += dist[37]
				if text[letter] == 'M':
					textreturn += dist[38]
				if text[letter] == 'N':
					textreturn += dist[39]
				if text[letter] == 'O':
					textreturn += dist[40]
				if text[letter] == 'P':
					textreturn += dist[41]
				if text[letter] == 'Q':
					textreturn += dist[42]
				if text[letter] == 'R':
					textreturn += dist[43]
				if text[letter] == 'S':
					textreturn += dist[44]
				if text[letter] == 'T':
					textreturn += dist[45]
				if text[letter] == 'U':
					textreturn += dist[46]
				if text[letter] == 'V':
					textreturn += dist[47]
				if text[letter] == 'W':
					textreturn += dist[48]
				if text[letter] == 'X':
					textreturn += dist[49]
				if text[letter] == 'Y':
					textreturn += dist[50]
				if text[letter] == 'Z':
					textreturn += dist[51]
				if text[letter] == 'а':
					textreturn += dist[52]
				if text[letter] == 'б':
					textreturn += dist[53]
				if text[letter] == 'в':
					textreturn += dist[54]
				if text[letter] == 'г':
					textreturn += dist[55]
				if text[letter] == 'д':
					textreturn += dist[56]
				if text[letter] == 'е':
					textreturn += dist[57]
				if text[letter] == 'ё':
					textreturn += dist[58]
				if text[letter] == 'ж':
					textreturn += dist[59]
				if text[letter] == 'з':
					textreturn += dist[60]
				if text[letter] == 'и':
					textreturn += dist[61]
				if text[letter] == 'й':
					textreturn += dist[62]
				if text[letter] == 'к':
					textreturn += dist[63]
				if text[letter] == 'л':
					textreturn += dist[64]
				if text[letter] == 'м':
					textreturn += dist[65]
				if text[letter] == 'н':
					textreturn += dist[66]
				if text[letter] == 'о':
					textreturn += dist[67]
				if text[letter] == 'п':
					textreturn += dist[68]
				if text[letter] == 'р':
					textreturn += dist[69]
				if text[letter] == 'с':
					textreturn += dist[70]
				if text[letter] == 'т':
					textreturn += dist[71]
				if text[letter] == 'у':
					textreturn += dist[72]
				if text[letter] == 'ф':
					textreturn += dist[73]
				if text[letter] == 'х':
					textreturn += dist[74]
				if text[letter] == 'ц':
					textreturn += dist[75]
				if text[letter] == 'ч':
					textreturn += dist[76]
				if text[letter] == 'ш':
					textreturn += dist[77]
				if text[letter] == 'щ':
					textreturn += dist[78]
				if text[letter] == 'ъ':
					textreturn += dist[79]
				if text[letter] == 'ы':
					textreturn += dist[80]
				if text[letter] == 'ь':
					textreturn += dist[81]
				if text[letter] == 'э':
					textreturn += dist[82]
				if text[letter] == 'ю':
					textreturn += dist[83]
				if text[letter] == 'я':
					textreturn += dist[84]
				if text[letter] == 'А':
					textreturn += dist[85]
				if text[letter] == 'Б':
					textreturn += dist[86]
				if text[letter] == 'В':
					textreturn += dist[87]
				if text[letter] == 'Г':
					textreturn += dist[88]
				if text[letter] == 'Д':
					textreturn += dist[89]
				if text[letter] == 'Е':
					textreturn += dist[90]
				if text[letter] == 'Ё':
					textreturn += dist[91]
				if text[letter] == 'Ж':
					textreturn += dist[92]
				if text[letter] == 'З':
					textreturn += dist[93]
				if text[letter] == 'И':
					textreturn += dist[94]
				if text[letter] == 'Й':
					textreturn += dist[95]
				if text[letter] == 'К':
					textreturn += dist[96]
				if text[letter] == 'Л':
					textreturn += dist[97]
				if text[letter] == 'М':
					textreturn += dist[98]
				if text[letter] == 'Н':
					textreturn += dist[99]
				if text[letter] == 'О':
					textreturn += dist[100]
				if text[letter] == 'П':
					textreturn += dist[101]
				if text[letter] == 'Р':
					textreturn += dist[102]
				if text[letter] == 'С':
					textreturn += dist[103]
				if text[letter] == 'Т':
					textreturn += dist[104]
				if text[letter] == 'У':
					textreturn += dist[105]
				if text[letter] == 'Ф':
					textreturn += dist[106]
				if text[letter] == 'Х':
					textreturn += dist[107]
				if text[letter] == 'Ц':
					textreturn += dist[108]
				if text[letter] == 'Ч':
					textreturn += dist[109]
				if text[letter] == 'Ш':
					textreturn += dist[110]
				if text[letter] == 'Щ':
					textreturn += dist[111]
				if text[letter] == 'Ъ':
					textreturn += dist[112]
				if text[letter] == 'Ы':
					textreturn += dist[113]
				if text[letter] == 'Ь':
					textreturn += dist[114]
				if text[letter] == 'Э':
					textreturn += dist[115]
				if text[letter] == 'Ю':
					textreturn += dist[116]
				if text[letter] == 'Я':
					textreturn += dist[117]
			else:
				textreturn += text[letter]
		return textreturn

	def decrypt(text):
		textreturn = ''
		length = len(text)
		cycle = 0
		while cycle < length:
			if text[cycle].isalpha():
				key = text[cycle] + text[cycle + 1] + text[cycle + 2] + text[cycle + 3]
				if key == dist[0]:
					textreturn += 'a'
				if key == dist[1]:
					textreturn += 'b'
				if key == dist[2]:
					textreturn += 'c'
				if key == dist[3]:
					textreturn += 'd'
				if key == dist[4]:
					textreturn += 'e'
				if key == dist[5]:
					textreturn += 'f'
				if key == dist[6]:
					textreturn += 'g'
				if key == dist[7]:
					textreturn += 'h'
				if key == dist[8]:
					textreturn += 'i'
				if key == dist[9]:
					textreturn += 'j'
				if key == dist[10]:
					textreturn += 'k'
				if key == dist[11]:
					textreturn += 'l'
				if key == dist[12]:
					textreturn += 'm'
				if key == dist[13]:
					textreturn += 'n'
				if key == dist[14]:
					textreturn += 'o'
				if key == dist[15]:
					textreturn += 'p'
				if key == dist[16]:
					textreturn += 'q'
				if key == dist[17]:
					textreturn += 'r'
				if key == dist[18]:
					textreturn += 's'
				if key == dist[19]:
					textreturn += 't'
				if key == dist[20]:
					textreturn += 'u'
				if key == dist[21]:
					textreturn += 'v'
				if key == dist[22]:
					textreturn += 'w'
				if key == dist[23]:
					textreturn += 'x'
				if key == dist[24]:
					textreturn += 'y'
				if key == dist[25]:
					textreturn += 'z'
				if key == dist[26]:
					textreturn += 'A'
				if key == dist[27]:
					textreturn += 'B'
				if key == dist[28]:
					textreturn += 'C'
				if key == dist[29]:
					textreturn += 'D'
				if key == dist[30]:
					textreturn += 'E'
				if key == dist[31]:
					textreturn += 'F'
				if key == dist[32]:
					textreturn += 'G'
				if key == dist[33]:
					textreturn += 'H'
				if key == dist[34]:
					textreturn += 'I'
				if key == dist[35]:
					textreturn += 'J'
				if key == dist[36]:
					textreturn += 'K'
				if key == dist[37]:
					textreturn += 'L'
				if key == dist[38]:
					textreturn += 'M'
				if key == dist[39]:
					textreturn += 'N'
				if key == dist[40]:
					textreturn += 'O'
				if key == dist[41]:
					textreturn += 'P'
				if key == dist[42]:
					textreturn += 'Q'
				if key == dist[43]:
					textreturn += 'R'
				if key == dist[44]:
					textreturn += 'S'
				if key == dist[45]:
					textreturn += 'T'
				if key == dist[46]:
					textreturn += 'U'
				if key == dist[47]:
					textreturn += 'V'
				if key == dist[48]:
					textreturn += 'W'
				if key == dist[49]:
					textreturn += 'X'
				if key == dist[50]:
					textreturn += 'Y'
				if key == dist[51]:
					textreturn += 'Z'
				if key == dist[52]:
					textreturn += 'а'
				if key == dist[53]:
					textreturn += 'б'
				if key == dist[54]:
					textreturn += 'в'
				if key == dist[55]:
					textreturn += 'г'
				if key == dist[56]:
					textreturn += 'д'
				if key == dist[57]:
					textreturn += 'е'
				if key == dist[58]:
					textreturn += 'ё'
				if key == dist[59]:
					textreturn += 'ж'
				if key == dist[60]:
					textreturn += 'з'
				if key == dist[61]:
					textreturn += 'и'
				if key == dist[62]:
					textreturn += 'й'
				if key == dist[63]:
					textreturn += 'к'
				if key == dist[64]:
					textreturn += 'л'
				if key == dist[65]:
					textreturn += 'м'
				if key == dist[66]:
					textreturn += 'н'
				if key == dist[67]:
					textreturn += 'о'
				if key == dist[68]:
					textreturn += 'п'
				if key == dist[69]:
					textreturn += 'р'
				if key == dist[70]:
					textreturn += 'с'
				if key == dist[71]:
					textreturn += 'т'
				if key == dist[72]:
					textreturn += 'у'
				if key == dist[73]:
					textreturn += 'ф'
				if key == dist[74]:
					textreturn += 'х'
				if key == dist[75]:
					textreturn += 'ц'
				if key == dist[76]:
					textreturn += 'ч'
				if key == dist[77]:
					textreturn += 'ш'
				if key == dist[78]:
					textreturn += 'щ'
				if key == dist[79]:
					textreturn += 'ъ'
				if key == dist[80]:
					textreturn += 'ы'
				if key == dist[81]:
					textreturn += 'ь'
				if key == dist[82]:
					textreturn += 'э'
				if key == dist[83]:
					textreturn += 'ю'
				if key == dist[84]:
					textreturn += 'я'
				if key == dist[85]:
					textreturn += 'А'
				if key == dist[86]:
					textreturn += 'Б'
				if key == dist[87]:
					textreturn += 'В'
				if key == dist[88]:
					textreturn += 'Г'
				if key == dist[89]:
					textreturn += 'Д'
				if key == dist[90]:
					textreturn += 'Е'
				if key == dist[91]:
					textreturn += 'Ё'
				if key == dist[92]:
					textreturn += 'Ж'
				if key == dist[93]:
					textreturn += 'З'
				if key == dist[94]:
					textreturn += 'И'
				if key == dist[95]:
					textreturn += 'Й'
				if key == dist[96]:
					textreturn += 'К'
				if key == dist[97]:
					textreturn += 'Л'
				if key == dist[98]:
					textreturn += 'М'
				if key == dist[99]:
					textreturn += 'Н'
				if key == dist[100]:
					textreturn += 'О'
				if key == dist[101]:
					textreturn += 'П'
				if key == dist[102]:
					textreturn += 'Р'
				if key == dist[103]:
					textreturn += 'С'
				if key == dist[104]:
					textreturn += 'Т'
				if key == dist[105]:
					textreturn += 'У'
				if key == dist[106]:
					textreturn += 'Ф'
				if key == dist[107]:
					textreturn += 'Х'
				if key == dist[108]:
					textreturn += 'Ц'
				if key == dist[109]:
					textreturn += 'Ч'
				if key == dist[110]:
					textreturn += 'Ш'
				if key == dist[111]:
					textreturn += 'Щ'
				if key == dist[112]:
					textreturn += 'Ъ'
				if key == dist[113]:
					textreturn += 'Ы'
				if key == dist[114]:
					textreturn += 'Ь'
				if key == dist[115]:
					textreturn += 'Э'
				if key == dist[116]:
					textreturn += 'Ю'
				if key == dist[117]:
					textreturn += 'Я'
				cycle += 4
			else:
				textreturn += text[cycle]
				cycle += 1
		return textreturn

	print('Goose Language Crypt/Decrypt')
	print('   Powered by ShiZZZeRRR    ')
	print('1) Зашифровать текст.')
	print('2) Дешифровать текст.')
	print('3) Что я умею?')
	print('4) Выход из программы.')

	choice = input('Введите номер нужной функции: ')

	if choice == '1':
		inputtext = input('Введите текст : ')
		print( crypt(inputtext) )
		input('Для перехода в меню нажмите Enter или введите любой текст : ')
	if choice == '2':
		inputtext = input('Введите текст : ')
		print( decrypt(inputtext) )
		input('Для перехода в меню нажмите Enter или введите любой текст : ')
	if choice == '3':
		print('Привет! Я умею переводить твой текст на гусиный язык и обратно.\nДля использования выбери соответствующие функции в меню.')
		input('Для перехода в меню нажмите Enter или введите любой текст : ')
	if choice == '4':
		sys.exit()

while 1 == 1:
	program()

Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> str1 = "hello"
>>> str2 = "Bob"
>>> bob = str1 + str2
>>> print(bob)
helloBob
>>> str3 = "123"
>>> x = int(str3) + 1
>>> print(x)
124
>>> name = input()
Chuck
>>> print(name)
Chuck
>>> apple = input()
100
>>> x = int(apple) - 10
>>> print(x)
90
>>> fruit = "banana"
>>> letter = fruit[1]
>>> print(letter)
a
>>> x = 3
>>> w = fruit[x - 1]
>>> print(w)
n
>>> fruit = "banana"
>>> print(len(fruit))
6
>>> fruit = "banana"
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(index, letter)
	index = index + 1

0 b
1 a
2 n
3 a
4 n
5 a
>>> fruit = "banana"
>>> for letter in fruit:
	print(letter)

	
b
a
n
a
n
a
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(index)
	index = index + 1

	
0
1
2
3
4
5
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
>>> 
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
b
a
n
a
n
a
>>> word = "banana"
>>> count = 0
>>> for letter in word:
	if letter == "a"
	
SyntaxError: invalid syntax
>>> for letter in word:
	if letter == "a":
		count = count + 1

>>> print(count)
3
>>> s = "Monty Python"
>>> print(s[0:4])
Mont
>>> print(s[6:7])
P
>>> print(s[6:20])
Python
>>> print(s[:2])
Mo
>>> print(s[8:])
thon
>>> print(s[:])
Monty Python
>>> a = "Hello"
>>> b = a + "There"
>>> print(b)
HelloThere
>>> c = a + " " + "There"
>>> print(c)
Hello There
>>> fruit = "banana"
>>> "n" in fruit
True
>>> "m" in fruit
False
>>> "nan" in fruit
True
>>> if "a" in fruit:
	print("Done!")

	
Done!
>>> if word == "banana":
	print("Bananas")

	
Bananas
>>> if word < "banana":
	print("Your word, " + word + ", comes before banana.")
	elif word > "banana":
		
SyntaxError: invalid syntax
>>> if word < "banana":
	print("Your word, " + word + ", comes before banana.")
	elif word > "banana":
		
SyntaxError: invalid syntax
>>> if word < "banana":
	print("Your word, " + word + ", comes before banana.")
elif word > "banana":
	print("Your word, " + word + ", comes after banana.")
else:
	print("Bananas")

	
Bananas
>>> greet = "Hello Bob"
>>> zap = greet.lower()
>>> print(zap)
hello bob
>>> print(greet)
Hello Bob
>>> print("Hi There".lower())
hi there
>>> fruit = "banana"
>>> pos = fruit.find("na")
>>> print(pos)
2
>>> aa = fruit.find("z")
>>> print(aa)
-1
>>> greet = "Hello Bob"
>>> nnn = greet.upper()
>>> print(nnn)
HELLO BOB
>>> www = greet.lower()
>>> print(www)
hello bob
>>> greet = "Hello Bob"
>>> nstr = greet.replace("Bob", "Jane")
>>> print(nstr)
Hello Jane
>>> nstr= greet.replace("o", "X")
>>> print(nstr)
HellX BXb
>>> greet = " Hello Bob "
>>> greet.lstrip()
'Hello Bob '
>>> greet.rstrip()
' Hello Bob'
>>> greet.strip()
'Hello Bob'
>>> line = "Pls have a n1 day"
>>> line.startswith("Pls")
True
>>> line.startswith("p")
False
>>> data = "asdadfaffafafaf@erere.rtu.lv"
>>> atpos = data.find("@")
>>> print(atpos)
15
>>> data = "asdadfaffafafaf@erere.rtu.lv 2018"
>>> sppos = data.find(" ", atpos)
>>> print(sppos)
28
>>> host = data[atpos + 1 : sppos]
>>> print(host)
erere.rtu.lv
>>> 

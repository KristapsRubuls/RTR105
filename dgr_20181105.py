Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> name = input("Enter: ")
Enter: Chuck
>>> name
'Chuck'
>>> apple = input("Enter: ")
Enter: 10
>>> x = int(apple) - 9
>>> print(x)
1
>>> fruit = "banana"
>>> letter = fruit[2]
>>> print(letter)
n
>>> x = 3
>>> w = fruit[x - 1]
>>> print(w)
n
>>> w = fruit[x - 2]
>>> print(w)
a
>>> fruit = "banana"
>>> print(len(fruit))
6
>>> fruit = "banana"
>>> x = len(fruit)
>>> print(x)
6
>>> fruit = "banana"
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(index, letter)
	index = index +1

	
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
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index +1

	
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index +1

	
b
a
n
a
n
a
>>> word = "banana"
>>> count = 0
>>> for letter in word:
	if letter == "a":
		count = count + 1
print(count)
SyntaxError: invalid syntax
>>> 
>>> for letter in word:
	if letter == "a":
		count = count + 1
	print(count)

	
0
1
1
2
2
3
>>> for letter in word:
	if letter == "a":
		count = count + 1

	
>>> 
>>> count
6
>>> for letter in "banana":
	print(letter)

	
b
a
n
a
n
a
>>> s = "Monty Python"
>>> print(s[6:10])
Pyth
>>> print(s[6:11])
Pytho
>>> print(s[6:12])
Python
>>> print(s[4:12])
y Python
>>> print(s[4:20])
y Python
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
	print("Found it!")

	
Found it!
>>> if word == "banana"
SyntaxError: invalid syntax
>>> if word == "banana":
	print("All right, bananas")

	
All right, bananas
>>> if word < "banana":
	print("Your word," + word + ", comes before banana")
elif:
	
SyntaxError: invalid syntax
>>> if word < "banana":
	print("Your word," + word + ", comes before banana")
	elif word > "banana":
		
SyntaxError: invalid syntax
>>> if word < "banana":
	print("Your word," + word + ", comes before banana")
elif word > "banana":
	print("Your word," + word + ", comes after banana")
else:
	print("All right, bananas")

	
All right, bananas
>>> greet = "Hello Bob"
>>> zap = greet.lower()
>>> print(zap)
hello bob
>>> print(greet)
Hello Bob
>>> print("Hi, There".lower())
hi, there
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
>>> nstr = greet.replace("o", "X)
			 
SyntaxError: EOL while scanning string literal
>>> nstr = greet.replace("o", "X")
			 
>>> print(nstr)
			 
HellX BXb
>>> 

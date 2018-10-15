Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> if x < 10:
	print("Smaller")

	
Smaller
>>> if x > 20:
	print("Bigger")

	
>>> 
>>> x > 20:
	
SyntaxError: invalid syntax
>>> 
>>> if x > 20:
	print("Bigger")
	print("Finis")

	
>>> 
>>> if x > 20:
	print("Bigger")
	else("Finis")
	
SyntaxError: invalid syntax
>>> x = 5
>>> if x == 5: print("Equals 5")

Equals 5
>>> if x > 4: print("Greater than 4")

Greater than 4
>>> if x >= 5: print("Greater than or Equals 5")

Greater than or Equals 5
>>> if x < 6: print("Less than 6")

Less than 6
>>> if x <= 5: print("Less than or Equals 5")

Less than or Equals 5
>>> if x != 6: print("Not equal 6")

Not equal 6
>>> x = 5
>>> print("Before 5")
Before 5
>>> if x == 5:
	print("Is 5")
	print("Is still 5")
	print("Third 5")

	
Is 5
Is still 5
Third 5
>>> print("Afterwards 5")
Afterwards 5
>>> print("Before 6")
Before 6
>>> if x == 6:
	print("Is 6")
	print("Is still 6")
	print("Third 6")

	
>>> print("Afterwards 6")
Afterwards 6
>>> x = 42
>>> if x > 1:
	print("More than one")
	if x < 100:
		print("Less then 100")
print("all done")
SyntaxError: invalid syntax
>>> x = 42
>>> if x > 1:
	print("More than one")
	if x < 100:
		print("Less then 100")
		
>>> x = 4
>>> if x > 2:
	print("Bigger")
else:
	print("Smaller")

	
Bigger
>>> if x < 2:
	print("Small")
elif x < 10:
	print("Medium")
else:
	print("Large")

Medium
>>> x = 0
>>> if x < 2:
	print("Small")
elif x < 10:
	print("Medium")
else:
	print("Large")

	
Small
>>> x = 5
>>> if x < 2:
	print("Small")
elif x < 10:
	print("Medium")
else:
	print("Large")

	
Medium
>>> x = 20
>>> if x < 2:
	print("Small")
elif x < 10:
	print("Medium")
else:
	print("Large")

	
Large
>>>  h 

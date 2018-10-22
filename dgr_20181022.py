Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> def computepay(hrs,rate):
	if nhrs <= 40:
    	print(nhrs * nrate)
	elif nhrs > 40:
    	n = nhrs - 40
	return (nrate * 40) + (n * nrate * 1.5)    

hrs = input("Enter Hours:")
nhrs = float(hrs)
rate = input("Enter the rate:")
nrate = float(rate)

p = computepay(nhrs,nrate)

print(p)

  File "<pyshell#0>", line 3
    print(nhrs * nrate)
        ^
IndentationError: expected an indented block
>>> def computepay(hrs,rate):
	if nhrs <= 40:
    	print(nhrs * nrate)
	elif nhrs > 40:
    	n = nhrs - 40
	return (nrate * 40) + (n * nrate * 1.5)    

hrs = input("Enter Hours:")
nhrs = float(hrs)
rate = input("Enter the rate:")
nrate = float(rate)

p = computepay(nhrs,nrate)
  File "<pyshell#1>", line 3
    print(nhrs * nrate)
        ^
IndentationError: expected an indented block
>>> hrs = input("Enter Hours:")
nhrs = float(hrs)
rate = input("Enter the rate:")
nrate = float(rate)
Enter Hours:45
>>> 
>>> 
>>> def computepay(hrs,rate):
	if nhrs <= 40:
    	print(nhrs * nrate)
	elif nhrs > 40:
    	n = nhrs - 40
	return (nrate * 40) + (n * nrate * 1.5)    

hrs = 45
nhrs = float(hrs)
rate = 10.50
nrate = float(rate)

p = computepay(nhrs,nrate)


  File "<pyshell#5>", line 3
    print(nhrs * nrate)
        ^
IndentationError: expected an indented block
>>> def computepay(hrs,rate):
	if nhrs <= 40:
		print(nhrs * nrate)
	elif nhrs > 40:
		n = nhrs - 40
	return (nrate * 40) + (n * nrate * 1.5)    

hrs = 45
nhrs = float(hrs)
rate = 10.50
nrate = float(rate)

p = computepay(nhrs,nrate)
SyntaxError: invalid syntax
>>> def computepay(hrs,rate):
	if nhrs <= 40:
		print(nhrs * nrate)
	elif nhrs > 40:
		n = nhrs - 40
	return (nrate * 40) + (n * nrate * 1.5)

hrs = 45
nhrs = float(hrs)
rate = 10.50

p = computepay(nhrs,nrate)
SyntaxError: invalid syntax
>>> hrs = 45
nhrs = float(hrs)
rate = 10.50
>>> def computepay(hrs,rate):
	if nhrs <= 40:
		print(nhrs * nrate)
	elif nhrs > 40:
		n = nhrs - 40
	return (nrate * 40) + (n * nrate * 1.5)

>>> p = computepay(nhrs,nrate)

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    p = computepay(nhrs,nrate)
NameError: name 'nhrs' is not defined
>>> def computepay(hrs,rate):
	if nhrs <= 40:
		print(nhrs * rate)
	elif nhrs > 40:
		n = nhrs - 40
	return (rate * 40) + (n * rate * 1.5)

>>> p = computepay(nhrs,rate)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    p = computepay(nhrs,rate)
NameError: name 'nhrs' is not defined
>>> p = computepay(hrs,rate)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    p = computepay(hrs,rate)
NameError: name 'rate' is not defined
>>> 

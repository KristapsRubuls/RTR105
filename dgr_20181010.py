Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> hrs = input(4)
4

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    hrs = input(4)
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> nano gyvfvy.py
SyntaxError: invalid syntax
>>> a = 5
>>> b = 2.3
>>> print(123)
123
>>> print(98.6)
98.6
>>> print("Hello worlds")
Hello worlds
>>> x = 12.2
>>> y = 14
>>> vars()
{'a': 5, 'b': 2.3, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 12.2, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> x = 100
>>> vars()
{'a': 5, 'b': 2.3, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> _speed

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    _speed
NameError: name '_speed' is not defined
>>> My_Name = "Kristaps"
>>> k = "Kristaps"
>>> My_name

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    My_name
NameError: name 'My_name' is not defined
>>> My_Name
'Kristaps'
>>> k
'Kristaps'
>>> a = 35.0
>>> type(a)
<type 'float'>
>>> b = 12.50
>>> c = a * b
>>> print(c)
437.5
>>> x = 2
>>> x = x + 2
>>> print(x)
4
>>> x = 0.6
>>> x = 3.9 * x * ( 1 - x )
>>> x
0.9359999999999999
>>> xx = 2
>>> xx = xx * 20
>>> xx
40
>>> jj = 23
>>> kk = jj / 5
>>> kk
4
>>> kk = jj % 5
>>> print(kk)
3
>>> print( 4 ** 3 )
64
>>> 4 ** 3
64
>>> eee = "helo"
>>> aaa = "worlds"
>>> print(eee + aaa)
heloworlds
>>> eee = "helo "
>>> print(eee + aaa)
helo worlds
>>> i = 42
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> type(f)
<type 'float'>
>>> sval = "123"
>>> type(sval)
<type 'str'>
>>> inval = int(sval)
>>> type(int)
<type 'type'>
>>> type(inval)
<type 'int'>
>>> print(inval + 1)
124
>>> name = input("Name?")
Name?Kristaps

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    name = input("Name?")
  File "<string>", line 1, in <module>
NameError: name 'Kristaps' is not defined
>>> print(name)

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(name)
NameError: name 'name' is not defined
>>> name

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> 

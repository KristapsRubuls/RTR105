Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> n = 5
>>> while n > 0:
	print(n)
	n = n - 1
print("Blastoff")
SyntaxError: invalid syntax
>>> while n > 0:
	print(n)
	n = n - 1

	
5
4
3
2
1
>>> while True:
	line = input("> ")
	if line == "done":
		break
	print(line)

	
> 

> helo there
helo there
> done
>>> while True:
	line = input("> ")
	if line[0] == "#":
		continue
	if line == "done":
		break
	print(line)
print("DOne!")
SyntaxError: invalid syntax
>>> while True:
	line = input("> ")
	if line[0] == "#":
		continue
	if line == "done":
		break
	print(line)

	
> # nub team
> print this
print this
> done
>>> for i in [5, 4, 3]:
	print(i)

	
5
4
3
>>> friends = ["Me", "Myself", "and I"]
>>> for friend in friends:
	print("Happy holidays: ", friend)

	
Happy holidays:  Me
Happy holidays:  Myself
Happy holidays:  and I
>>> for thing in [9, 41, 12, 3]
SyntaxError: invalid syntax
>>> for thing in [9, 41, 12, 3]:
	print(thing)

	
9
41
12
3
>>> largest_so_far = -1
>>> print("Before", largest_so_far)
Before -1
>>> for num in [9, 41, 12, 3]:
	if num > largest_so_far:
		largest_so_far = num
	print(largest_so_far, num)

	
9 9
41 41
41 12
41 3
>>> zork = 0
>>> for num in [9, 41, 12, 3]:
	zork = zork + 1
	print(zork, num)

	
1 9
2 41
3 12
4 3
>>> zork = 0
>>> for num in [9, 41, 12, 3]:
	zork = zork + num
	print(zork, num)

	
9 9
50 41
62 12
65 3
>>> count = 0
>>> sum = 0
>>> for num in [9, 41, 12, 3]:
	count = count + 1
	sum = sum + num
	print(count, sum, num, sum/count)

	
1 9 9 9.0
2 50 41 25.0
3 62 12 20.666666666666668
4 65 3 16.25
>>> for num in [9, 41, 12, 3]:
	if num > 20:
		print("Largest number", num)

		
Largest number 41
>>> found = False
>>> for num in [9, 41, 12, 3]:
	if num == 3:
		found = True
	print(found, num)

	
False 9
False 41
False 12
True 3
>>> largest_so_far = -1
>>> for num in [9, 41, 12, 3]:
	if num > largest_so_far:
		largest_so_far = num
	print(largest_so_far)

	
9
41
41
41
>>> for num in [9, 41, 12, 3]:
	if num > largest_so_far:
		largest_so_far = num
	print(largest_so_far, num)

	
41 9
41 41
41 12
41 3
>>> smallest_so_far = -1
>>> for num in [9, 41, 12, 3]:
	if num < smallest_so_far:
		smallest_so_far = num
	print(smallest_so_far, num)

	
-1 9
-1 41
-1 12
-1 3
>>> smallest = None
>>> for num in [9, 41, 12, 3]:
	if smallest is None:
		smallest = num
	elif num < smallest:
		smallest = num
	print(smallest, num)

	
9 9
9 41
9 12
3 3
>>> 

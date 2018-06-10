#! python3
import sys
print(sys.version)



print("Print me")
# indentation is important, 
x = 1 
if x == 1:
	# indented 4 spaces or one tab
	print("x is 1.")

myFloat = 7.0
myint = 7
myFloat = float(7)
print(myint)
print(myFloat)

myString = 'hello'
mystring = "hello"
print(mystring)

mystring = "Don't worry about apostrophes"
print(mystring)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = str(three) + " " + world
print (helloworld)

a, b = 3, 4
print(a, b)


print (a, b)       # prints repr((x, y))
print((a, b))
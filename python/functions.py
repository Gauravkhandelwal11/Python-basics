import math 
print(math.pi)


import math as m 
print(m.pi)
print(m.cos(36.87))

 
from math import cos
print(cos(36.87))

# To import all file use *

from math import *
print(cos(45))
print(sin(90))
print(pi)


# User defined:- 

def greet():
    print("Good morning")

greet()
greet()
greet()
greet()
greet()
greet()
greet()
greet()


def greet(name,dish):
	print("good morning", name)
	print("please have" , dish)


greet("Gaurav","Cake")


# returning function

def sumoflist(a):
	print("calculating....")
	return sum(a)

marks = [55,78,98,95]
sumofmarks = sumoflist(marks)
print("my sum of marks = " , sumofmarks)















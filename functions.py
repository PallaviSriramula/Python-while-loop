"""
FUNCTIONS:
    A function is a block of code which is used to run a feature
    multiple times just by calling it.
    The functions written by the programmer is called user defined funtions
    A function has three parts function declaration,
    function definition and function calling.

    Synatax: def func_name():
                # block of code  

    Funtion only runs when you call it
    Uses:
    Code reusability
    Shorter and cleaner program
    Easy debugging

    Types of functions:
    1. Functions with no arguments or return
    2. Functions with return
    3. Functions with arguments
    4. Functions with both arguments and returns
"""

# basic function intro
def greetings(): # function declaration
    print('Welcome') # function definition

greetings() # function calling
greetings()

# write a function to print numbers from range 1 to 10
def numPrinter():
    for i in range(1,11):
        print(i,end=' ')
    print()
numPrinter()
numPrinter()

# WAF to even number
def evenChecker():
    num = int(input("Enter the number:"))
    if num%2==0:
        print("Even number")
    else:
        print("Not even number")
evenChecker()

# WAF to print sum of numbers from 1 to 25
def sumOfNum():
    i = 1
    sum = 0
    while i<=25:
        sum+=i
        i+=1
    print(f"Sum of numbers from 1 to 25 = {sum}")
sumOfNum()

# Write a function to print num from 10 to 1 using for loop
def reverseNum():
    for i in range(10,0,-1):
        print(i)
reverseNum()

# Write a function to print revers of a number
def reverseNum():
    num = int(input("Enter the number: "))
    rev = 0
    while num>0:
        digit = num%10
        rev = rev * 10 + digit
        num//=10
    print(rev)
reverseNum()

# write a function to print greatest among three numbers
def greatestNum():
    num = int(input("Enter the number: "))
    digit = 0
    greatest = 0
    while num > 0:
        digit = num%10
        if digit>greatest:
            greatest = digit
        num//=10
    print(greatest)
greatestNum() 

# WAF to print all factors of 24
def factors():
    num = int(input("Enter the number: "))
    i = 2
    while i<num:
        if num%i==0:
            print(f"Factors = {i}",end=' ')
        i+=1
factors()

# WAF to check whether a number is automorphic or not
"""
AUTOMORPHIC - number which ends with itself when it is squared
eg = 5 **2 = 25 ending with 5
25**2 = 625 ending with 25
76**2 = 5776 ends with 76
"""
num=int(input("Enter the number:"))
temp=num
square=num*num
while temp > 0:
    if square % 10 != temp % 10:
        print(f"{num} is not an automorphic number")
        break
    square//=10
    temp//=10
else:
    print(f"{num} is an automorphic number")
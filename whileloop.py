# Create a Python program that uses a while loop to ask the user for a number until they enter a positive integer.

num = -1
while num <= 0:
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input! Please enter an integer.")
        num = -1
sum = 0
i = 1
while i <= num:
    sum = sum + i
    i = i + 1
print("Sum of numbers from 1 to", num, "is", sum)
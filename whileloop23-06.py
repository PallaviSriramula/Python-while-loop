# COUNT VALID AGES
"""
Keep accepting ages until the user enters -1. Ignore ages below 1 and above 120. 
Count valid ages only.
"""
count = 0
age = 0
while age != -1:
    age = int(input("Enter your age(-1 to stop)"))
    if age == -1:
        continue
    if age<1 or age>120:
        continue
    count+=1

print(f"Valid ages = {count}")

# SUM MULTIPLES OF 5
"""
Keep accepting numbers until the user enters 0. Add only numbers divisible by 5. 
Skip all other numbers using continue.
"""
sum = 0
number =-1
while number!=0:
    number = int(input("Enter the numbers(0 to stop): "))
    if number==0:
        continue
    elif number%5!=0:
        continue
    sum+=number
print(f"Sum = {sum}")

# Count Upper case letters
"""
Given: text = "PyTHon ProGRAM" Count how many uppercase letters are present. 
Skip all other characters using continue.
"""
text = "PyTHon ProGRAM"
count = 0
for char in text:
    if 'A' <= char <= 'Z':
        count+=1
    else:
        continue
print(f"Uppercase letters count = {count}")

# Total Sales amount
"""
sales = [500, 0, 1200, 0, 700] Find the total sales amount. Entries with value 0 represent 
cancelled sales and should be skipped using continue.
"""
sales = [500,0,1200,0,700]
sum = 0
for amount in sales:
    if amount==0:
        continue
    else:
        sum+=amount
print(f"Total sales amount = {sum}")
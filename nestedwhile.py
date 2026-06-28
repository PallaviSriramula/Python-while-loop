# Generate all pairs from 1–5 and print only pairs whose sum is even.
i=1
while i<=5:
    sum = 0
    j = 1
    while j<=5:
        sum = i+j
        if sum%2==0:
            print(f"{i},{j}")
        j+=1
    i+=1

# Generate all pairs from 1–10 and print only pairs whose product is greater than 30. Also count total pairs.
i = 1
product=1
count = 0
while i<=10:
    j=1
    while j<=10:
        product = i*j
        if product>30:
            print(f"({i},{j}) -> {product}")
            count+=1
        j+=1
    i+=1
print(f"Number of pairs = {count}")

# Keep asking user for numbers until 0 is entered. For each number, find factors and their sum.
num = int(input("Enter the number(0 to stop): "))
while num!=0:
    sum = 0
    print("Factors:", end = " ")
    for i in range(1,num+1):
        if num%i==0:
            print(i,end=" ")
            sum += i
        else:
            continue
    print()
    print(f"Sum = {sum}")
    num = int(input("Enter the number (0 to stop): "))

# Given numbers=[12,7,20,9], for each number print values from 1 to that number and count evens.

numbers = [12, 7, 20, 9]
for num in numbers:
    i = 1
    count = 0
    while i <= num:
        if i % 2 == 0:
            count += 1
        i += 1
    print(f"{num} → Even count: {count}")
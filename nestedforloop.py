# Student marks Total
"""
There are 5 students and each student has marks in 3 subjects. 
Calculate and print the total marks of each student.
"""
marks = [
    [70, 80, 90],
    [60, 75, 85],
    [90, 95, 80],
    [55, 65, 70],
    [88, 76, 91]
]
student = 1
for i in marks:
    total = 0
    for j in i:
        total += j
    print("Student", student, "Total =", total)
    student += 1

# SHOP SAlES REPORT
"""
 A shop sells 4 products. For each product, enter sales for 7 days and find the total sales.
"""
sales = [
    [100, 200, 150, 120, 180, 140, 110],
    [90, 160, 130, 150, 170, 180, 140],
    [200, 210, 220, 190, 180, 175, 160],
    [80, 95, 100, 110, 120, 130, 140]
]
product = 1
for i in sales:
    total = 0
    for j in i:
        total += j
    print("Product", product, "Total Sales =", total)
    product += 1

# Find Highest Mark in Each Student Record
"""
There are 4 students and each student has marks in 5 subjects. 
Find the highest mark scored by each student.
"""
marks = [
    [70, 85, 60, 90, 75],
    [88, 76, 91, 80, 67],
    [55, 60, 58, 62, 59],
    [95, 89, 93, 90, 87]
]
student = 1
for i in marks:
    highest = i[0]
    for j in i:
        if j > highest:
            highest = j
    print("Student", student, "Highest Mark =", highest)
    student += 1

# Theatre Seat Booking Status
"""
A theatre has 5 rows and 6 seats in each row. Input seat status (1=Booked, 0=Empty). 
Count booked seats in each row.
"""
seats = [
    [1, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 1]
]
row = 1
for i in seats:
    booked = 0
    for j in i:
        if j == 1:
            booked += 1
    print("Row", row, "Booked Seats =", booked)
    row += 1
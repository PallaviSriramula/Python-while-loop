def display_student(student_id, name):
    print("\nStudent Details")
    print("Student ID:", student_id)
    print("Student Name:", name)

def calculate_total(mark1, mark2, mark3, mark4, mark5):
    total = mark1 + mark2 + mark3 + mark4 + mark5
    print("\nTotal Marks:", total)

def calculate_percentage(mark1, mark2, mark3, mark4, mark5):
    total = mark1 + mark2 + mark3 + mark4 + mark5
    percentage = total / 5
    print("Percentage:", percentage)

    find_grade(percentage)

def find_grade(percentage):
    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 75:
        print("Grade: B")
    elif percentage >= 60:
        print("Grade: C")
    elif percentage >= 40:
        print("Grade: D")
    else:
        print("Grade: Fail")

def highest_mark(mark1, mark2, mark3, mark4, mark5):
    highest = mark1
    if mark2 > highest:
        highest = mark2
    if mark3 > highest:
        highest = mark3
    if mark4 > highest:
        highest = mark4
    if mark5 > highest:
        highest = mark5
    print("Highest Mark:", highest)

def lowest_mark(mark1, mark2, mark3, mark4, mark5):
    lowest = mark1
    if mark2 < lowest:
        lowest = mark2
    if mark3 < lowest:
        lowest = mark3
    if mark4 < lowest:
        lowest = mark4
    if mark5 < lowest:
        lowest = mark5
    print("Lowest Mark:", lowest)

def pass_fail(mark1, mark2, mark3, mark4, mark5):
    if mark1 < 35 or mark2 < 35 or mark3 < 35 or mark4 < 35 or mark5 < 35:
        print("\nResult: Fail")
    else:
        print("\nResult: Pass")

student_id = input("Enter Student ID: ")
name = input("Enter Student Name: ")

mark1 = int(input("Enter Subject 1 Marks: "))
mark2 = int(input("Enter Subject 2 Marks: "))
mark3 = int(input("Enter Subject 3 Marks: "))
mark4 = int(input("Enter Subject 4 Marks: "))
mark5 = int(input("Enter Subject 5 Marks: "))

display_student(student_id, name)
calculate_total(mark1, mark2, mark3, mark4, mark5)
calculate_percentage(mark1, mark2, mark3, mark4, mark5)
highest_mark(mark1, mark2, mark3, mark4, mark5)
lowest_mark(mark1, mark2, mark3, mark4, mark5)
pass_fail(mark1, mark2, mark3, mark4, mark5)
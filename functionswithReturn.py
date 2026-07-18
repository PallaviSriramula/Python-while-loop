def calculate_total(subject_marks):
    total = 0
    for mark in subject_marks.values():
        total = total + mark
    return total

def calculate_average(total, count):
    average = total / count
    return average

def assignment_contribution(average, assignment_score):
    average = average + (assignment_score * 0.10)
    return average

def attendance_check(average, attendance):
    if attendance < 75:
        average = average - 5
        status = "Attendance Below 75%"
    else:
        status = "Good Attendance"
    return average, status

def add_extracurricular(average, points):
    average = average + points
    return average

def find_grade(average):
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "Fail"
    return grade

def failed_subjects(subject_marks):
    failed = []
    for subject in subject_marks:
        if subject_marks[subject] < 35:
            failed.append(subject)
    return failed

def result(failed):
    if len(failed) == 0:
        return "Pass"
    else:
        return "Fail"

def process_student_results(student_id, student_name, subject_marks,
                            attendance_percentage,
                            assignment_score,
                            extracurricular_points):
    total = calculate_total(subject_marks)
    average = calculate_average(total, 5)
    average = assignment_contribution(average, assignment_score)
    average, attendance_status = attendance_check(average,
                                                  attendance_percentage)
    average = add_extracurricular(average,
                                  extracurricular_points)
    grade = find_grade(average)
    failed = failed_subjects(subject_marks)
    final_result = result(failed)
    return student_id, student_name, total, average, grade, attendance_status, failed, final_result

student_id = input("Enter Student ID: ")
student_name = input("Enter Student Name: ")
subject_marks = {}
subject_marks["Math"] = int(input("Enter Math Marks: "))
subject_marks["Science"] = int(input("Enter Science Marks: "))
subject_marks["English"] = int(input("Enter English Marks: "))
subject_marks["Computer"] = int(input("Enter Computer Marks: "))
subject_marks["Physics"] = int(input("Enter Physics Marks: "))
attendance_percentage = int(input("Enter Attendance Percentage: "))
assignment_score = int(input("Enter Assignment Score: "))
extracurricular_points = int(input("Enter Extracurricular Points: "))

student_id, student_name, total, average, grade, attendance_status, failed, final_result = process_student_results(
    student_id,
    student_name,
    subject_marks,
    attendance_percentage,
    assignment_score,
    extracurricular_points
)

print("\nStudent ID:", student_id)
print("Student Name:", student_name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)
print("Attendance Status:", attendance_status)
print("Failed Subjects:", failed)
print("Result:", final_result)
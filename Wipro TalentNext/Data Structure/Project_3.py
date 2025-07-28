student_marks = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

name = input("Enter a name: ")

marks = student_marks.get(name)

if marks:
    average = sum(marks) / len(marks)
    print("Average percentage mark:", average)
else:
    print("Student not found.")
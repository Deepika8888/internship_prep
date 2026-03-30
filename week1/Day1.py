

import csv


def student_summary(name, age, grade):
    return f"{name} is {age} years old and scored {grade}"


students = [
    {"name": "Alice", "age": 20, "grade": 85},
    {"name": "Bob", "age": 22, "grade": 90},
    {"name": "Charlie", "age": 21, "grade": 78}
]


print("=== Student Summaries ===")
for student in students:
    print(student_summary(student["name"], student["age"], student["grade"]))



with open("students.txt", "w") as file:
    for student in students:
        file.write(student_summary(student["name"], student["age"], student["grade"]) + "\n")

print("\n=== Written to students.txt ===")

# Reading from .txt file
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())


with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "grade"])
    for student in students:
        writer.writerow([student["name"], student["age"], student["grade"]])

print("\n=== Written to students.csv ===")

# Reading from CSV file
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']} | Age: {row['age']} | Grade: {row['grade']}")
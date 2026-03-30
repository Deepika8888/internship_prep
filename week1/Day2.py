

print("=== FizzBuzz (1-30) ===")
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


print("\n=== Guess the Number ===")
print("Guess a number between 1 and 10")
guess = int(input("Your guess: "))
while guess != 7:
    print("Wrong! Try again.")
    guess = int(input("Your guess: "))
print("Correct!")



def check_number(n):
    if n > 20:
        print(f"High: {n}")
    else:
        print(f"Low: {n}")

print("\n=== High / Low Numbers ===")
numbers = [12, 45, 7, 23, 89]
for number in numbers:
    check_number(number)



def check_grade(name, grade):
    if grade > 80:
        print(f"Pass: {name} scored {grade}")
    else:
        print(f"Fail: {name} scored {grade}")

students = [
    {"name": "Alice", "age": 20, "grade": 85},
    {"name": "Bob", "age": 22, "grade": 90},
    {"name": "Charlie", "age": 21, "grade": 78}
]

print("\n=== Student Pass/Fail ===")
for student in students:
    check_grade(student["name"], student["grade"])
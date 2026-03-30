


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def summary(self):
        print(f"{self.name} is {self.age} years old and scored {self.grade}")

    def is_pass(self):
        if self.grade > 40:
            print(f"{self.name} passed")
        else:
            print(f"{self.name} failed")


# Creating objects
student1 = Student("Alice", 20, 85)
student2 = Student("Bob", 22, 90)
student3 = Student("Charlie", 21, 38)

# Calling methods
student1.summary()
student1.is_pass()

student2.summary()
student2.is_pass()

student3.summary()
student3.is_pass()
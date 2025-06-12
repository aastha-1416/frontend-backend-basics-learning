'''
Types of Inheritance:
Single Inheritance: A child class inherits from a single parent class.
Multiple Inheritance: A child class inherits from more than one parent class.
Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
Hybrid Inheritance: A combination of two or more types of inheritance.
'''
# 1. Single Inheritance

class Person:
    def info(self):
        print("I am a person.")

class Student(Person):  # Inherits from Person
    def study(self):
        print("I am studying.")

# 2. Multilevel Inheritance

class SchoolStudent(Student):  # Inherits from Student
    def school_level(self):
        print("I am a school student.")

# 3. Hierarchical Inheritance

class Teacher(Person):  # Another class inheriting from Person
    def teach(self):
        print("I am teaching.")


# 4. Multiple Inheritance

class Artist:
    def draw(self):
        print("I can draw.")

class Engineer(Person, Artist):  # Inherits from both Person and Artist
    def build(self):
        print("I can build things.")

# 5. Hybrid Inheritance (mix of types)

class CollegeStudent(Student, Artist):  # Hybrid: Student (Single) + Artist (Multiple)
    def college_life(self):
        print("I am a college student who can also draw.")


# Testing All

print("---- Single Inheritance ----")
s1 = Student()
s1.info()
s1.study()

print("\n---- Multilevel Inheritance ----")
s2 = SchoolStudent()
s2.info()
s2.study()
s2.school_level()

print("\n---- Hierarchical Inheritance ----")
t1 = Teacher()
t1.info()
t1.teach()

print("\n---- Multiple Inheritance ----")
e1 = Engineer()
e1.info()
e1.draw()
e1.build()

print("\n---- Hybrid Inheritance ----")
c1 = CollegeStudent()
c1.info()
c1.study()
c1.draw()
c1.college_life()

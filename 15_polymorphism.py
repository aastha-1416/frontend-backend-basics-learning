#Polymorphism allows methods to have the same name but behave differently based on the object's context.

class Person:
    def role(self):
        print("I am a generic person.")

class Student(Person):
    def role(self):
        print("I am a student, I study.")

class Teacher(Person):
    def role(self):
        print("I am a teacher, I teach.")

class Engineer(Person):
    def role(self):
        print("I am an engineer, I build things.")

class CollegeStudent(Student):
    def role(self):
        print("I am a college student, I study and have fun.")
def show_role(p):
    p.role()

people = [Person(), Student(), Teacher(), Engineer(), CollegeStudent()]

for person in people:
    show_role(person)
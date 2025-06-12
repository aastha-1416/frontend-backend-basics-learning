'''
Abstraction means hiding the implementation and showing only essential features, typically done using abstract classes.
Encapsulation means wrapping data (variables) and methods into a single unit (class), and using private or protected attributes to restrict access.

abc stands for Abstract Base Classes.
'''
from abc import ABC, abstractmethod

# Abstraction: Base abstract class
class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def role(self):
        pass

# Student class with Encapsulation
class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.__marks = marks  # Encapsulation: private variable

    def role(self):
        print(f"{self.name} is a student.")

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks!")

# Teacher class (abstraction only)
class Teacher(Person):
    def role(self):
        print(f"{self.name} is a teacher.")

# Test the combined behavior
s1 = Student("Aarav", 88)
t1 = Teacher("Ms. Meera")

s1.role()
print("Marks:", s1.get_marks())
s1.set_marks(95)
print("Updated Marks:", s1.get_marks())

t1.role()

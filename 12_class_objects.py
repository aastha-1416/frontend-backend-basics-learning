class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def display_info(self):
      print(f"Name: {self.name}, Age: {self.age}")

# Create objects
per1 = Person("Annie", 18)
per2 = Person("Skiee", 20)

# Access object attributes
print("name of 1st persom",per1.name)
print("name of 2nd persom",per2.name)
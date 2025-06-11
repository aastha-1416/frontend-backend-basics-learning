#Local Variables
def sum(x,y):
   sum = x + y
   return sum
print(sum(5, 10))

# Global Variables
x = 5
y = 10
def sum():
   sum = x + y
   return sum
print(sum())

#multiple variable
name="Annie"
age=18
city="Munbai"
print(name)
print(age)
print(city)
print("My name is", name )
print("I'm", age, "year old and I live in", city)
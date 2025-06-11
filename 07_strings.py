#Printing Strings

name = "annie"
city = "mumbai"
print("I'm", name, "I live in", city)

#Multiline Strings

a = """I am Annie,I lives in Mumbai.I am 18 years old"""

b = '''i am annie,i lives in mumbai.i am 18 years old'''

print(a)
print(b)

#Slicing Strings

test = "Hello, World!"
print(test[2:5])
print(test[0:])
print(test[:13])
print(test[:5])

#String Concatenation
name = "Annie"
surname = "Shah"

person = name + " " + surname
print(person)

#String Format syntax:f"string {expression}"

name = "Annie"
age = 18
person = f"My name is {name}, I am {age} years old"
print(person)

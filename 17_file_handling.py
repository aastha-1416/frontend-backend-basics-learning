# Reading a File in Read Mode (r)
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

#Reading a File in Binary Mode (rb)
file = open("example.txt", "rb")
content = file.read()
print(content)
file.close()

#Writing to a File
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()

#Writing to a File in Append Mode (a)

file = open('example.txt', 'a')
file.write("This will add this line")
file.close()

#Handling Exceptions When Closing a File
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()
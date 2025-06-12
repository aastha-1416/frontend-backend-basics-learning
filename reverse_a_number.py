num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10 #Gets the last digit
    rev = rev * 10 + digit #Builds reversed number
    num = num // 10 #Removes the last digit

print("Reversed number:", rev)
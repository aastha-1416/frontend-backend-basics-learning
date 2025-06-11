print ("Calculator")
while True:
	num1=input("Enter a Number")
	num1=float(num1)
	num2=input("Enter a Number")
	num2=float(num2)

	print ("choose one operator: +,-,*,/")
	operator=input("Enter an operator")

	if operator=='+':
		result=num1+num2
		print("resuly is:",result)
	elif operator=='-':
		result=num1-num2
		print("resuly is:",result)
	elif operator=='*':
		result=num1*num2
		print("resuly is:",result)
	elif operator=='/':
		result=num1/num2
		print("resuly is:",result)
	else:
		print ("Invalid operator")

	again = input("Do you want to calculate again? Type 'yes' to continue or 'exit' to stop: ")
	if again == "yes":
		continue
	else:
		print("Exit")
		break
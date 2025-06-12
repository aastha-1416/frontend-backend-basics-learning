'''
The follow keywords (blocks) are used with exception handling −

try − Write the main code on which you want to test the exception.
except − Write code to handle the exception.
else − Write code to execute when there is no error.
finally − Write code to execute finally no matter there is an error or not.
'''

# Create function to divide two numbers
def divide_numbers(a, b):
   try:
      result = a / b
   except ZeroDivisionError:
      print("Error: Cannot divide by zero!")
   else:
      print(f"The divide result is : {result}")
   finally:
      print("Execution complete.")

# Calling function
print("Test Case 1:")
divide_numbers(10, 2)

print("\nTest Case 2:")
divide_numbers(10, 0)
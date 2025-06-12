import math
import random
import datetime
import os
import sys
import statistics

# Function 1: Use math module
def calculate_math():
    print("Square root of 16 is:", math.sqrt(16))
    print("Factorial of 5 is:", math.factorial(5))

# Function 2: Use random module
def generate_random():
    print("Random number between 1 and 10:", random.randint(1, 10))
    print("Random choice from list:", random.choice(['apple', 'banana', 'cherry']))

# Function 3: Use datetime module
def show_time():
    now = datetime.datetime.now()
    print("Current date and time:", now)
    print("Today’s date:", now.date())

# Function 4: Use os module
def check_os():
    print("Current working directory:", os.getcwd())
    print("List of files in current directory:", os.listdir('.'))

# Function 5: Use sys module
def system_info():
    print("Python version info:", sys.version)
    print("Platform:", sys.platform)

# Function 6: Use statistics module
def stats_demo():
    data = [10, 20, 30, 40, 30]
    print("Mean:", statistics.mean(data))
    print("Median:", statistics.median(data))
    print("Mode:", statistics.mode(data))

# Call all functions
calculate_math()
print("------")
generate_random()
print("------")
show_time()
print("------")
check_os()
print("------")
system_info()
print("------")
stats_demo()

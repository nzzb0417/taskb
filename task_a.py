import sys

try:
    grade = int(input("Please enter your final grade as an integer: "))
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if grade > 100 or grade < 0:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if grade <= 39:
    print(f"{grade} is a Fail")
elif grade >= 40 and grade <= 69:
    print(f"{grade} is a Pass")
elif grade > 69 and grade <= 100:
    print(f"{grade} is a Distinction")

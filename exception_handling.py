"""
age = int(input('Age: '))
print(age)


# when we run the above program if we give valid input we dont have any issues, the program will execute successfully
# with exit code 0 ( terminated successfully with no errors
# But if we give invalid data like "asd" the program crashes with exit code 1 and type of error as ValueError,
# when we work on User interface, we should get user friendly messages
# So, we can do this be handling exceptions. As a programmer we would not want the entire program to crash because user
# entered invalid data
# While giving invalid data notice the type of the error and exit code
# we can handle using the construct called Try Except

# input  = asd
# if we give value as asd, we get invalid age error with exit code 0, means system did not crash
try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print("Invalid age")
"""
# we can encounter different types of error
# provide age as 0 in above example, we will get ZeroDivisionError: division by zero error and exit code 1,
#  so it means we have not anticipated and handled this error

# input = 0
# program executes successfully with exit code 0, system did not crash
try:
    age = int(input('Age: '))
    income = 30000
    risk = income/age
    print(age)
except ValueError:
    print("Invalid age")
except ZeroDivisionError:
    print("Age cannot be 0")







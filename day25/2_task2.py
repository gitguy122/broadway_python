# take two numbers input and divide a number by another number . Handle the possible exceptions

try:
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter another number"))
    result = num1 / num2
    print(result)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Enter number other than 0")
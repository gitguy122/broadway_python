# Take two numbers as input and add those numbers.Handle the possible exceptions
try:
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
except ValueError:
    print("Please provide  a valid number")
else:
    summ = num1 + num2
    print(summ)

# Exceptions in Python are handled using try ...except block

# Try...except
try:
    num = int(input("Enter a Number"))
    print(num)
except ValueError:
    print("Please do it nicely fker")

# it is not mandatory to mention error type in except block.If it is not mentioned then it can not handle
# all the exceptions


# We can handle as many errors as possible

# try...except
try:
    num = int(input("Enter a number"))
    result = 23 / num
    print(result)
except ValueError:
    print("Please provide a valid number")
except ZeroDivisionError:
    print("do other than this")

# try...except...else
try:
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
    result = 23 / num1, num2
    print(result)
except ValueError:
    print("Please provide a valid number")
except ZeroDivisionError:
    print("do other than this")
else:
    summ = num1 + num2
    prod = num1 * num2
    print(summ)
    print(prod)

# try...except...else...finally
# finally block is always executed regardless of errors or not.


try:
    f = open("test.txt", "w")
except:
    print("something went wrong")
else:
    print(f)
finally:
    f.close()
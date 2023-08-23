num = int(input("enter a number"))
if (num % 2) == 0:
    print(f"{num} is Even number")
else:
    print(f"{num} is an Odd number")


# task 2
num1 = int(input("enter your first number"))
num2 = int(input("enter your second number"))
num3 = int(input("enter your third number"))
if (num1 > num2) and (num1 > numb3):
    a = num1
elif(num2 > num1) and (num2 > num3):
    a = num2
else:
    a = num3
print("the greatest number is ",a)

# task 3
score = float input("enter score")
if score > 0 or score < 1:
    raise ValueError
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print(D)
elif score >= 0.5:
    print(E)
else:
    print(5)


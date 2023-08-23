n = int(input("enter a numnber"))
counter = 0
for i in range(1, n+1):
    if n % i ==0:
        counter += 1
if sum == 2:
    print(f"{n} is a prime number")
else:
    print(f"{n} is a composite")
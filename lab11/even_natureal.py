n = int(input("Enter a number: "))
s = 0
for i in range(2, n+1, 2):
    s += i
print(f"The sum of even natural numbers up to {n} is: {s}")

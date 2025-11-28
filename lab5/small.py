a,b=map(int, input("enter two integers seprated by space: ").split())
if a<b:
    print(f"{a} is smaller than {b}")
elif a>b:
    print(f"{b} is smaller than {a}")
else:
    print("Both numbers are equal")
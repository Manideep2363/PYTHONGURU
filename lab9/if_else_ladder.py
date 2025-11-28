a = input("press any key: ")
if a.isdigit():
    print(f"{a} is a number")
elif a.islower():
    print(f"{a} is a lowercase letter")
elif a.isupper():
    print(f"{a} is an uppercase letter")
else:
    print(f"{a} is a special character")
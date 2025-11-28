c = input("Enter a character in lowercase: ")
if c.islower():
    print(f'{c} in uppercase is {c.upper()}')
else:
    print(f'{c} is not a lowercase character')
c = 0
ch = input("Enter a character: ")

while ch != '$':
    c += 1
    ch = input("Enter a $ to stop: ")
print(f"The number of characters entered is: {c}")
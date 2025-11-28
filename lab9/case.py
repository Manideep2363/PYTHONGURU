c = input("Enter a character: ")
match True:
    case _ if c.isdigit():
        print(f'{c} is a number')
    case _ if c.isupper():
        print(f'{c} is uppercase')
    case _ if c.islower():
        print(f'{c} is lowercase')
    case _ :
        print(f'{c} is a special character')
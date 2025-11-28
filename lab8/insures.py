m = input('enter your marital status (single/married): ').strip().lower()
s=input('enter sex (male/female): ').strip().lower()
age=int(input('enter your age: '))
if m=='married':
    print("Your are eligible for insurance")
else:
    if s=='male'and age>30:
        print("You are eligible for insurance")
    elif s=='female' and age>25:
        print("You are eligible for insurance")
    else:
        print("You are not eligible for insurance")
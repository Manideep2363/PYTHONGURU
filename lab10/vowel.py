c = input("Enter a vowel character(a, e, i, o, u): ")
match True:
    case _ if c == 'a':
        print(f'apple')
    case _ if c == 'e':
        print(f'elephant')
    case _ if c == 'i':
        print(f'ice-cream')
    case _ if c == 'o':
        print(f'orange')
    case _ if c == 'u':
        print(f'umbrella')
    case _ :
        print(f'The character {c} is not a vowel')

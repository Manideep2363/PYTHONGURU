for i in range(4):
    for j in range(i):
        print(' ', end=' ')
    for k in range(5 - i):
        print(k+1, end=' ')
    print()
for i in range(5,0,-1):
    for j in range(5-i):
        print(end='  ')
    for k in range(i):
        print(i, end='  ')
    print()
for i in range(2,6):
    for j in range(6-i-1):
        print(end='  ')
    for k in range(i):
        print(i, end='  ')   
    print()

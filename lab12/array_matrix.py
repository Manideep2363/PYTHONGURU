a=list(map(int,input("Enter the elements of the array: ").split()))
for i in range(3):
    for j in range(3):
        print(a[i*3 + j], end=" ")
    print()
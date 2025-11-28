a=int(input("enter side a: "))
b=int(input("enter side b: "))
c=int(input("enter side c: "))
s=(a+b+c)/2
print(f'area of triangle with 3 sides:{(s*(s-a)*(s-b)*(s-c))**0.5}')
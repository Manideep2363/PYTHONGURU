a, b, c = map(int, input('Enter three sides of the triangfele separated by space: ').split())
if (a*a)+(b*b)==(c*c) or (b*b)+(c*c)==(a*a) or (c*c)+(a*a)==(b*b):
    print("The triangle is a right-angled triangle")
elif (a==b) and (b==c):
    print("The triangle is an equilateral triangle")
elif (a==b) or (b==c) or (c==a):
    print("The triangle is an isosceles triangle")
else:
    print("The triangle is a scalene triangle")
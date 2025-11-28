a, b, c = map(int, input("enter three numbers separated by space: ").split())
d=b**2 - 4*a*c
if d>0:
    r1 = (-b + d**0.5) / (2*a)
    r2 = (-b - d**0.5) / (2*a)
    print(f"The roots are real and different: {r1} and {r2}")
elif d==0:
    r = -b / (2*a)
    print(f"The roots are real and the same: {r}")
else:
    real_part = -b / (2*a)
    imag_part = (-d)**0.5 / (2*a)
    print(f"The roots are complex and different: {real_part}+{imag_part}i and {real_part}-{imag_part}i")
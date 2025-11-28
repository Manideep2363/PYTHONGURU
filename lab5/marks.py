a, b, c = map(int, input("enter marks of three subjects seprated by space: ").split())
total = a + b + c
average = total / 3
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Grade: {grade}")
print(f"Total marks: {total}")
print(f"Average marks: {average}")
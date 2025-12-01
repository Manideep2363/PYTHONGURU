a=[1,2,3,3,4,5,5,5]
distinct_list = []
s = 0
for i in a:
    if i not in distinct_list:
        distinct_list.append(i)
        s += i
print(f"The sum of distinct elements is: {s}")
    
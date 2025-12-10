e = [(1, 'Nick $$#  Jr.', 23, '45000.0$'), 
     (2, 'Nick Jr.', 63, '245000.0&**&'),
     (3, 'Nick Sr.', 53, 145000.0),
     (4, 'Dan  ^^', 23, '45000.0'),
     (5, 'Steve',23,46000.0)]
unw=''.join([chr(i) for i in range(32,32 +15)] + \
            [chr(i) for i in range(32+26, 32+26+7)] + ['^'])
cleaned_employees = []
for emp in e:
    _id, name, age, sal = emp
    new_name = ''.join([ch for ch in name if ch not in unw])
    new_name = new_name.replace('Jr', ' jr').replace('Sr', ' sr')
    new_sal =float(str(sal).strip(unw))
    cleaned_employees.append((_id, new_name, age, new_sal))

print(f'Desending order:{sorted(cleaned_employees, key=lambda x: x[3], reverse=True)}')
print(f'Acending order:{sorted(cleaned_employees, key=lambda x: x[3])}')

_max=max(cleaned_employees, key=lambda x: x[-1])[-1]
_min=min(cleaned_employees, key=lambda x:x[-1])[-1]

for i in cleaned_employees:
    if _max==i[-1]:
        print(f'employees with heighest salaries:{i[1]}')
    if _min==i[-1]:
        print(f'employees with least salaries:{i[1]}')


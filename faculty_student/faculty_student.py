import csv

st=[]
sub={}
fac={}
with open("/mnt/c/Users/HP/Downloads/faculties_data.csv",'r') as f:
    data=csv.reader(f)
    # next(data)
    for i in data:
        fac[i[0]] = i[1]
with open("/mnt/c/Users/HP/Downloads/students_data.csv",'r') as f:
    data = csv.reader(f)
    for i in data:
        st.append(i)

# for i in st:
#     if int(i[-1]) >90:
#         fac_id = i[1]
#         if fac_id not in sub:
#             sub[fac_id] = 1
#         else :
#             sub[fac_id]+=1

# tfac=max(sub.items(), key=lambda x:x[1])[0]
# print(fac[tfac])
# print(sub[tfac])

#2
# total ={}
# passed={}
# for i in st:
#     faculty_id = i[1]
#     percentage = int(i[-1])

#     if faculty_id not in total:
#         total[faculty_id] =1
#     else:
#         total[faculty_id]+=1


#     if percentage >40:
#         if faculty_id not in passed:
#             passed[faculty_id] =1
#         else:
#             passed[faculty_id] +=1
# pass_percent ={}
# for fid in total:
#     pass_percent[fid] = (passed.get(fid, 0) / total[fid]) * 100
# top_faculty_id =max(pass_percent.items(),key=lambda x:x[1])[0]
# print(fac[top_faculty_id])
# print(round(pass_percent[top_faculty_id],2),"%")

#3
# total ={}
# passed = {}
# for i in st:
#     f =i[1]
#     per =int(i[-1])

#     if f not in total:
#         total[f]=1
#     else:
#         total[f]+=1

#     if per > 40:
#         if f not in passed:
#             passed[f]=1
#         else:
#             passed[f]+=1
# pass_percentage ={}
# for fid in total:
#     pass_percentage[f] = (passed.get(f,0) / total[f])*100
# top_faculty_id=min(pass_percentage.items(),key=lambda x:x[1])[0]
# print(fac[top_faculty_id])
# print(round(pass_percent[top_faculty_id],2),"%")

#4
# top_st=st[0]
# max_tot=int(st[0][-1])

# for i in st:
#     total = int(i[-1])

#     if total>max_tot:
#         max_tot=total
#         top_st=i[0]
# print(top_st)
# print(max_tot)

#5
# for i in st:
#     if i[1] == "Mathematics":
#         d[i[0]] = int(i[-1])
# top = max(d.items(), key=lambda x:x[1])[0]
# print(top)
        
#for each student
# d={}
# for i in st:
#     if i[0] not in d:
#         d[i[0]]=int(i[-1])
#     else:
#         d[i[0]] += int(i[-1])
# s={}
# for n,m in d.items():
#     s[n]=round(m/len(fac),2)
# print(s)

#6
#for each subject
# total={}
# count={}
# for i in st:
#     subject =i[1]
#     marks=int(i[-1])

#     if marks > 40:
#         total[subject] = total.get(subject,0) + marks
#         count[subject] = count.get(subject,0) + 1
# avg={}
# for sub in total:
#     avg[sub] =round(total[sub]/count[sub],2)
# print(avg)

#7
d={}
for i in st:
    if i[0] not in d:
        d[i[0]]=int(i[-1])
    else:
        d[i[0]] += int(i[-1])
mini=min(d,key=lambda x:d[x])
print(mini)
print(d[mini])
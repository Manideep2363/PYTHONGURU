b_sal=int(input("Enter basic salary: "))

da=40
hra=20

gross_sal=b_sal+((da*b_sal)/100)+((hra*b_sal)/100)
print(f"The gross salary is: {gross_sal}")
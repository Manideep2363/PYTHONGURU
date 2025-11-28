principal_amount=int(input("Enter principal amount: "))
rate_of_interest=int(input("Enter rate of interest: "))
time=int(input("Enter time in years: "))
#simple interest
si=(principal_amount*rate_of_interest*time)/100
#compound interest
ci=principal_amount*(1 + rate_of_interest/100)**time - principal_amount
print(f'Simple Interest is {si}')
print(f'Compound Interest is {ci}')
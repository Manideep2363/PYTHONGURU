seconds=int(input("enter seconds:"))

hours=seconds//3600
minutes=(seconds%3600)//60
sec=(seconds%3600)%60

print(f"{hours} hours:{minutes} minutes:{sec} seconds")
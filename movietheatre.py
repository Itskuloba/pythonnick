# write a python program to calculate the price of a theatre based on the age of the customer
# 0-5 years=free
# 6-12 years=500
# 13-17 years=1000
# 18+ years=1500

age = int(input("Enter your age"))
if age <= 5:
    print("Free")
elif age >= 6 and age <= 12:
    print("500/=")
elif age >= 13 and age <= 17:
    print("1000/=")
else:
    print("1500/=")

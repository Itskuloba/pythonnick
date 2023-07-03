#create a python program to check if a given year is leap. The year is divisible by 4 but not divisible by 100. Except if it is divisible by 400
year=int(input("Input year"))

if year % 4 == 0 and (year %100 !=0 or year % 400 == 0 ):
    print("Its a leap year")

else:
    print("Not a leap year")
#write a python program to calculate the tick price for a movie theater based on the age

import calendar
year = int(input("Enter your year:>>>\t"))

if calendar.isleap(year):
    print("leap year")
else:
    print("not a leap year")

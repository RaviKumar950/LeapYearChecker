years = int(input("Enter your year:>>>\t"))

if (years % 400 ==0)or(years % 4==0 and years % 100 != 0):
    print(years,"Is the leap year")
else:
    print(years,"This year is not leap year")
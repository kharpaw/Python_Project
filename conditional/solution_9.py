year = 2032

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "Is a lipear")
else:
    print("Not a lipear")
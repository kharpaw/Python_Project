age = int(input("Enter you age: "))
day = "wednesday"
price = 12 if age >= 18 else 8

if day.lower() == "Wednesday":
    price -= 2

print(price)

print("Ticker price for you is #", price)
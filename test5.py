#5: Exchange currencies
#1 USD = 0.75 GBP
#1 USD = 0.89 Euro
#1 USD = 145.87

x = int(input("Enter amount in USD: "))
y = int(input("1 for Eur, 2 for GBP, 3 for JPY: "))

if y == 1:
    result = float(x * 0.89)
elif y == 2:
    result = float(x * 0.75)
elif y == 3:
    result = float(x * 145.87)

print(result)
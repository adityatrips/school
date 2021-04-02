p = float(input("ENTER PRINCIPLE (p)\n=> "))
r = float(input("ENTER RATE OF INTEREST (r)=> "))
n = int(input("ENTER COMPOUNDS PER YEAR (n)\n=> "))
t = int(input("ENTER YEARS (y)\n=> "))

amt = p*(1+(r/n))**(n*t)

print(f"FINAL AMOUNT: {amt}")

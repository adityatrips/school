p = float(input("ENTER PRINCIPLE\n=> "))
r = float(input("ENTER RATE OF INTEREST\n=> "))
t = float(input("ENTER THE TIME PERIOD\n=> "))
si = (p * r * t) / 100
amt = p + si
print(f"The interest is {si}")
print(f"The amount is {amt}")

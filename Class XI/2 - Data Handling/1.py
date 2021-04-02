p = float(input("ENTER PRINCIPLE\n=> "))
r = float(input("ENTER RATE\n=> "))
t = float(input("ENTER TIME\n=> "))
si = (p * r * t) / 100
amt = p + si
print(f"SI: {si}")
print(f"AMT: {amt}")

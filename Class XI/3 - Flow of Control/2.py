item = int(input("HOW MANY ITEMS WOULD YOU LIKE TO BUY\n=> "))
if item < 10:
  print(f"Cost: {item * 120}")
elif 99 < item < 10:
  print(f"Cost: {item * 100}")
else:
  print(f"Cost: {item * 70}")

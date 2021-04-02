ages = list(map(int, input("ENTER AGES SEPARATED BY A SPACE\n=> ").split()))
grp1 = 0
grp2 = 0
grp3 = 0

for age in ages:
  if age > 26 and age < 35:
    grp1 += 1
  elif age > 36 and age < 45:
    grp2 += 1
  elif age > 46 and age < 55:
    grp3 += 1

print(f"26-35: {grp1}")
print(f"36-45: {grp2}")
print(f"46-55: {grp3}")

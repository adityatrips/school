def add2dict(d, key, val):
  d[key] = val


names = list(map(str, input("ENTER NAMES\n=> ").split()))
salaries = list(map(int, input("ENTER RESPECTIVE SALARY\n=> ").split()))

d = {}

for x in range(len(names)):
  add2dict(d, names[x], salaries[x])

print(d)

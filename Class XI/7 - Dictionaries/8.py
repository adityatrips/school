def add2dict(d, k, v):
  d[k] = v


d = eval(input("ENTER A DICTIONARY\n=> "))
new_d = {}

for key, val in d.items():
  add2dict(new_d, val, key)
print(new_d)

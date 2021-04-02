def add2dict(d, k, v):
  d[k] = v


d = eval(input("ENTER A DICT LIKE {key: [num1, num2],...}\n=> "))
new_d = {}
for key, val in d.items():
  s = 0
  for n in val:
    s += n
  add2dict(new_d, key, s)

print(new_d)

name = []
ph = []
d = {}


def add2dict(key, val):
  d[key] = val


n = int(input("ENTER HOW MANY CONTACTS\n=> "))

for i in range(n):
  name = input("ENTER NAME\n=> ")
  ph = int(input("ENTER PHONE NUMBER\n=> "))
  add2dict(name, ph)
  print()

for key, val in d.items():
  print(f'Key: {key}\tValue: {val}')

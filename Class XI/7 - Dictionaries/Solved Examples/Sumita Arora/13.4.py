name = []
marks = []
d = {}


def add2dict(key, val):
  d[key] = val


n = int(input("ENTER HOW MANY CONTACTS\n=> "))

for i in range(n):
  name = input("ENTER NAME\n=> ")
  marks = float(input("ENTER MARKS\n=> "))
  add2dict(name, marks)

if 89.9 in d.values():
  print("Has 89.9")
else:
  print("No 89.9")

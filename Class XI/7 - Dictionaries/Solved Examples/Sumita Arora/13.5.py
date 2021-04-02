M = {}
n = int(input("ENTER HOW MANY STUDENTS\n=> "))


def add2dict(key, val):
  M[key] = val


for _ in range(n):
  r, m = eval(input("ENTER ROLL NUMBER, MARKS\n=> "))
  add2dict(r, m)

print(M)

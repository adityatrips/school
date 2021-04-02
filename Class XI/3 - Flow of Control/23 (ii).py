x = int(input("ENTER X\n=> "))
n = int(input("ENTER N\n=> "))
s = 0

for i in range(x, n+1):
  s += ((x**i)/i)
  print(f"({x}^{i})/{i}")
print(x+s)

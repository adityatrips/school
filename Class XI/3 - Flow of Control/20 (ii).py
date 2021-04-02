s = 0
n = int(input("ENTER N\n=> "))

for i in range(1, n+1):
  if i % 2 == 1:
    s += i**2
  else:
    None
print(f"Sum is {s}")

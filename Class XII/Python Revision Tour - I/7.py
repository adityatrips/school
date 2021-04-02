n = int(input("ENTER A NUMBER\n >> "))
if n > 0:
  print(sum(range(n, 2*n)))
elif n < 0:
  print(sum(range(2*n, n, -1)))
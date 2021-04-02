n = int(input("ENTER N\n=> "))
m = int(input("ENTER M\n=> "))
for i in range(1, n+1):
  if i % m == 0:
    if i % 2 == 0:
      print(f"{i}: Even")
    else:
      print(f'{i}: Odd')

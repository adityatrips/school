nbr = int(input("ENTER THE NUMBER\n=> "))

for i in range(2, (nbr * (1/2))):
  if nbr % i == 0:
    print("Not prime")
    break
else:
  print(f"Is prime!")

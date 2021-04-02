a = float(input("ENTER SIDE A\n=> "))
b = float(input("ENTER SIDE B\n=> "))
c = float(input("ENTER SIDE C\n=> "))

if (a + b > c) and (b + c > a) and (a + c > b):
  print("Triangle possible")
else:
  print("Triangle not possible")

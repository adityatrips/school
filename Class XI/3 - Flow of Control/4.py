x = float(input("ENTER X\n=> "))
y = float(input("ENTER Y\n=> "))
if x > y:
  if x - y == 0.001:
    print("Close")
  else:
    print("Not close")
else:
  if y - x == 0.001:
    print("Close")
  else:
    print("Not close")

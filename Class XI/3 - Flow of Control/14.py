n = int(input("ENTER N GREATER THAN 20\n=> "))
if n < 20:
  print("Didn't you read, GREATER than 20")
else:
  for i in range(11, n+1):
    if i % 3 == 0 and i % 7 == 0:
      print(f"{i}: TipsyTopsy")
    elif i % 3 == 0:
      print(f"{i}: Tipsy")
    elif i % 7 == 0:
      print(f"{i}: Topsy")

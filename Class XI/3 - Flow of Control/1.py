cm = float(input("ENTER LENGTH IN CM\n=> "))
if cm < 0:
  print("Invalid Entry")
else:
  inch = cm / 2.54
  print(f"{cm} cm in inches is {inch}!")

celsius = float(input("ENTER TEMPERATURE IN CELSIUS\n=> "))
if celsius < 273.15:
  print("Invalid! No temperature can be below absolute zero!")
elif celsius == 273.15:
  print("Temperature is absolute zero!")
elif 273.15 < celsius < 0:
  print("Temperature is below freezing!")
elif celsius == 0:
  print("Temperature at freezing point!")
elif 0 > celsius > 100:
  print("Temperature is in normal range!")
elif celsius > 100:
  print("Temperature is above the boiling point!")

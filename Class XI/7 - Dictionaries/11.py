d1 = eval(input("ENTER DICT 1\n=> "))
d2 = eval(input("ENTER DICT 2\n=> "))

for key, val in d1.items():
  for key2, val2 in d2.items():
    if key == key2 and val2 == val:
      print("Contained")
      pass

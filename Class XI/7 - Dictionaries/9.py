d1 = eval(input("ENTER DICT 1\n=> "))
d2 = eval(input("ENTER DICT 2\n=> "))

overlapping_keys = []

for key1 in d1.keys():
  for key2 in d2.keys():
    if key1 == key2:
      overlapping_keys.append(key1)
print(overlapping_keys)

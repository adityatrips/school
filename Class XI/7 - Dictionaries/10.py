d1 = eval(input("ENTER DICT 1\n=> "))
d2 = eval(input("ENTER DICT 2\n=> "))

cnt = 0

for key, val in d1.items():
  for key2, val2 in d2.items():
    if val == val2:
      cnt += 1

print(cnt, 'keys have same values')

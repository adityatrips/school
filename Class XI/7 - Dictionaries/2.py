def add2dict(d, key, val):
  d[key] = val


s = input("ENTER A STRING\n=> ")

letter_count = {}

for char in s:
  add2dict(letter_count, char, s.count(char))

print(letter_count)

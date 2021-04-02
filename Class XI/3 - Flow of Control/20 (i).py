n = 2
d = 9
s = 0
for i in range(1, 8):
  t = n / d
  if i % 2 == 0:
    t = t * -1
  print(f"{n}/{d}")
  s += t
  n += 3
  d += 4
print(f"Sum is {s}")

t = ((2, 5), (4, 2), (9, 8), (12, 10))
count = 0
for tup in t:
    if tup[0] % 2 == 0 and tup[1] % 2 == 0:
        count += 1

print("Even pairs:", count)

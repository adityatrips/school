lst = list(range(1, 21))
slice1 = lst[5:15:2]
slice2 = lst[::4]
s1_sum = 0
s2_sum = 0

print("SLICE 1")
for el in slice1:
    print(el, end=' ')
    s1_sum += el
print()
print("Sum of slice two:", s1_sum)
print("Average of slice one:", sum(slice1)/len(slice1))
print()
print("SLICE 2")
for el in slice2:
    print(el, end=' ')
    s2_sum += el
print()
print("Sum of slice two:", s2_sum)
print("Average of slice two:", sum(slice2)/len(slice2))

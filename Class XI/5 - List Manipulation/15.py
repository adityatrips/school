lst1 = eval(input("ENTER LIST 1\n=> "))
lst2 = eval(input("ENTER LIST 2\n=> "))

index = 0

for l1item in lst1:
    for l2item in lst2:
        if l2item != l1item:
            index = lst1.index(l1item)
print(index)

lst = []
r = int(input("Enter how many rows?\n=> "))
c = int(input("Enter how many cols?\n=> "))
for i in range(r):
    row = []
    for j in range(c):
        el = int(input(f"Enter element at {i}, {j}: "))
        row.append(el)
    lst.append(row)
print("List created is:", lst)

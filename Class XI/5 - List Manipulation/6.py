lst = eval(input("ENTER A LIST\n=> "))
num = int(input("ENTER A NUMBER\n=> "))
found_index = []
err = []

for i in range(len(lst)):
    if num == lst[i]:
        found_index.append(i)
    else:
        err.append("No suitable entry found")

if len(found_index) == 0:
    for e in err:
        print(e)
else:
    for i in found_index:
        print(f"Number found @ index {i}")

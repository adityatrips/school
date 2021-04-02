lst = eval(input("Enter a list\n=> "))
el = eval(input("Enter the element to count the frequency\n=> "))
count = 0
for i in range(lst):
    if i == el:
        count += 1
    else:
        count += 0
if count == 0:
    print(f"Element {el} not found!")
else:
    print(f"Element {el} found {count} times")

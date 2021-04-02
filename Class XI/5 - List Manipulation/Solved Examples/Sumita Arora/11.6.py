lst = list(range(1, 11))
print("Existing list:", lst)
n = eval(input("Enter a list\n=> "))
if type(n) == type([]):
    lst.extend(n)
    print("New List:", lst)
elif type(n) == type(1):
    lst.append(n)
    print("New List:", lst)
else:
    print("Enter either list or a number")

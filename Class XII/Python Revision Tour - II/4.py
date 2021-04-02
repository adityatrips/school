x = eval(input("ENTER LIST\n >> "))
lst = []

lst.insert(0, x[-1])
for i in range(len(x)):
    lst.append(x[i])
lst.pop(-1)

print(lst)

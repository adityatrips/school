lst = eval(input("ENTER A LIST\n=> "))
slst = sorted(lst)
print("SORTED LIST",)
for i in range(len(slst)-1):
    if slst[i] == slst[i+1]:
        slst.pop(i)
        slst.insert(-1, slst[i])

print("List:", slst)

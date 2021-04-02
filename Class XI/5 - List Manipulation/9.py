l1 = eval(input("ENTER A LIST\n=> "))
lnew = []

lnew.insert(0, l1[-1])
for index, item in enumerate(l1):
    lnew.insert(item, index+1)
lnew.pop(-1)
print(lnew)

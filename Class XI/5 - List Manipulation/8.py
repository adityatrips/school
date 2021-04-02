l1 = eval(input("ENTER LIST ONE\n=> "))
l2 = eval(input("ENTER LIST TWO\n=> "))
l3 = []

for index in range(len(l1)):
    l3.append(l1[index]+l2[index])

print(l3)

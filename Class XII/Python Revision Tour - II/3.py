x = eval(input("ENTER A LIST\n >> "))
y = eval(input("ENTER A LIST AGAIN\n >> "))
rslt = []

for i in range(len(x)):
    rslt.append(x[i] + y[i])

print(rslt)

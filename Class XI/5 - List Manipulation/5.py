lst = eval(input("ENTER A LIST OF STRINGS\n=> "))

for i in range(len(lst)):
    lst[i] = lst[i][1:]
print(f'New list: {lst}')

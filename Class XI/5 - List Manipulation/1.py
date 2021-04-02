lst = eval(input("ENTER A LIST\n=> "))
inc = int(input("ENTER INCREMENT VALUE\n=> "))
print(f'Original: {lst}')
for i in range(len(lst)):
    lst[i] += inc
print(f'New list: {lst}')

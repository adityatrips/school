lst = eval(input("ENTER A LIST OF NUMBERS BETWEEN 1-12\n=> "))
for index in range(len(lst)):
    if lst[index] > 10:
        lst[index] = 10
print(f'New list: {lst}')

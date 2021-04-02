lst = eval(input("ENTER A LIST\n=> "))
start = int(input("START INDEX\n=> "))
end = int(input("END INDEX\n=> "))
lst_slice = lst[start:end]
print(f'Maximum of the slice: {max(lst_slice)}')
print(f'Minimum of the slice: {min(lst_slice)}')

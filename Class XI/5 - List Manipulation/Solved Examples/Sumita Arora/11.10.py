lst = eval(input("Enter a list\n=> "))
len_lst = len(lst)
mean, s = 0, 0
for el in lst:
    s += el
print('Sum of all elements / Length of the sequece = Mean')
print(f'{s} / {len_lst} = {s/len_lst}')

lst1 = eval(input("Enter a list 1\n=> "))
lst2 = eval(input("Enter a list 2\n=> "))

mx1 = max(lst1)
mx2 = max(lst2)

if mx1 >= mx2:
    print(f'{mx1} is at index {lst2.index(mx1)}')
else:
    print(f'{mx2} is at index {lst2.index(mx2)}')

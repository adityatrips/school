lst = eval(input("Enter a list\n=> "))
lst_min = min(lst)
for i, el in enumerate(lst):
    if el == lst_min:
        print("Minimum:", el, 'at index', i)
        break

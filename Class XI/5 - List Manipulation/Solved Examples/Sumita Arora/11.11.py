lst = eval(input("Enter a list\n=> "))
srch = eval(input("Enter the search query\n=> "))
for i, el in enumerate(lst):
    if el == srch:
        print(f'{el} found at index {i}')
        break

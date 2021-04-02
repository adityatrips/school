def unit(n1, n2):
    if int(n1[-1]) > int(n2[-1]):
        return f'{n1} is greater'
    else:
        return f'{n2} is greater'


n1 = input("ENTER A NUMBER\n >> ")
n2 = input("ENTER A NUMBER\n >> ")

print(unit(n1, n2))

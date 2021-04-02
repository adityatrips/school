lst = eval(input("Enter a list\n=> "))
ln = len(lst)//2
mx = max(lst)
mx_ind = lst.index(mx)

if mx_ind < ln:
    print("First half")
elif mx_ind > ln:
    print("Second half")
else:
    print("Middle")

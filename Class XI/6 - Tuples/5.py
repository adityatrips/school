f_t = ()
for i in range(5):
    row = ()
    for j in range(5):
        t = int(input(f'Enter element for ({i}, {j})\n=> '))
        row += (t,)
    f_t += (row,)
print("Final Tuple", f_t)

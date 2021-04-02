f_t = ()
for i in range(5):
    row = ()
    for j in range(5):
        t = int(input(f'Enter element for ({i}, {j})\n=> '))
        row += (t,)
    f_t += (row,)

print(
    f"Student 1 has a total of {sum(f_t[0])} marks and has an average of {sum(f_t[0])/5}"
)
print(
    f"Student 1 has a total of {sum(f_t[1])} marks and has an average of {sum(f_t[1])/5}"
)
print(
    f"Student 1 has a total of {sum(f_t[2])} marks and has an average of {sum(f_t[2])/5}"
)
print(
    f"Student 1 has a total of {sum(f_t[3])} marks and has an average of {sum(f_t[3])/5}"
)
print(
    f"Student 1 has a total of {sum(f_t[4])} marks and has an average of {sum(f_t[4])/5}"
)

num = eval(input("ENTER A LIST OF NUMERATORS\n=> "))
denum = eval(input("ENTER A LIST OF DENOMINATORS\n=> "))
global tmp
tmp = ''
fraction = []
max_of_denum = max(denum)
for d in denum:
    if max_of_denum == d:
        tmp = denum.index(d)
max_relative_of_num = int(tmp)

frac = max_of_denum/num[max_relative_of_num]
for i in range(len(denum)):
    if num[i]/denum[i] < frac:
        fraction.insert(0, num[i])
        fraction.insert(1, denum[i])
print(f"Smallest fraction: {fraction[0]} / {fraction[1]}")

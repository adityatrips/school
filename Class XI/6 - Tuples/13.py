import statistics

int_tuple = eval(input("ENTER A TUPLE OF NUMERIC VALUES\n=> "))

mode_el = None
mode = 0

for i in range(len(int_tuple)):
    if int_tuple.count(i) > mode:
        mode = int_tuple.count(i)
        mode_el = int_tuple[i]-1
    else:
        continue
print(f'{mode_el} occurs {mode} times')

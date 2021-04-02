seq_a = eval(input("ENTER SEQUENCE A\n=> "))
seq_b = eval(input("ENTER SEQUENCE B\n=> "))
is_same = False

for i in range(len(seq_a)):
    if seq_a[i] == seq_b[i]:
        is_same = True
    else:
        is_same = False
        break

if is_same:
    print("True")
else:
    print("False")

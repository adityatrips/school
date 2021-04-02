n = int(input("NUMBER OF STUDENTS\n=> "))
stdata = ()
for i in range(n):
    s = eval(input(f"ENTER TUPLE OF ROLL NO., NAME, MARKS FOR STUDENT {i+1}"))
    stdata += (s,)
print(stdata)

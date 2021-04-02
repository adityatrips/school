alphabet_lst = ()
lst = ()
for i in range(97, 123):
    alphabet_lst += (chr(i),)

for j in range(1, 27):
    lst += (alphabet_lst[j-1]*j,)

print(lst)

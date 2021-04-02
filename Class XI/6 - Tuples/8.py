str_tuple = eval(input("ENTER A TUPLE OF STRINGS\n=> "))
lens = ()
for i in str_tuple:
    lens += (len(i),)
print(min(lens))
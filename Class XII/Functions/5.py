def is_len_equal(st1, st2):
    if len(st1) == len(st2):
        return True
    else:
        return False


st1 = input("ENTER A STRING\n >> ")
st2 = input("ENTER A STRING\n >> ")

if is_len_equal(st1, st2):
    print("Equal")
else:
    print("Unequal")

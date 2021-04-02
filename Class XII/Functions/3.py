def cube(num=2):
    print(f"Cube of {num} is {num**3}")


def is_char_equal(ch1, ch2):
    if ch1 == ch2:
        return True
    else:
        return False


print("1=Cube")
print("2=Char check")
dec = input("ENTER YOUR DECISION\n >> ")
while dec not in [1, 2]:
    dec = input("ENTER YOUR DECISION\n >> ")
if dec == 1:
    num = int(input("ENTER A NUMBER TO CALCULATE CUBE\n >> "))
    cube(num)
elif dec == 2:
    ch1 = input("ENTER CHAR ONE\n >> ")
    ch2 = input("ENTER CHAR TWO\n >> ")
    if is_char_equal(ch1, ch2):
        print("Equal")
    else:
        print("Not equal")

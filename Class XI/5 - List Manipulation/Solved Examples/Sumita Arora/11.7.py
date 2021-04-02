lst = []
print(f'The list is {lst}')
running = True
while running:
    print("MAIN MENU")
    print("1. INSERTION MENU")
    print("2. DELETIONMENU")
    print("3. EXIT")

    main_dec = int(input("ENTER YOUR DECISION\n=> "))
    if main_dec == 1:
        print("INSERTION MENU")
        print("1. INSERT AT LAST")
        print("2. INSERT AT START")
        print("3. INSERT AT A PARTICULAR INDEX")

        ins_dec = int(input("ENTER YOUR DECISION\n=> "))
        if ins_dec == 1:
            elem = eval(input("ENTER THE ELEMENT\n=> "))
            lst.append(elem)
            print(f'GREAT NOW THE LIST IS')
            print(lst)
        elif ins_dec == 2:
            elem = eval(input("ENTER THE ELEMENT\n=> "))
            lst.insert(0, elem)
            print(f'GREAT NOW THE LIST IS')
            print(lst)
        elif ins_dec == 3:
            elem = eval(input("ENTER THE ELEMENT\n=> "))
            pos = int(input("ENTER THE POSITION\n=> "))
            lst.insert(pos, elem)
            print(f'GREAT NOW THE LIST IS')
            print(lst)
        else:
            print("WRONG INPUT!")

    elif main_dec == 2:
        print("DELETION MENU")
        print("1. DELETE AT LAST")
        print("2. DELETE AT START")
        print("3. DELETE AT A PARTICULAR INDEX")

        del_dec = int(input("ENTER YOUR DECISION\n=> "))
        if del_dec == 1:
            lst.pop(-1)
            print(f'GREAT NOW THE LIST IS')
            print(lst)
        elif del_dec == 2:
            lst.pop(0)
            print(f'GREAT NOW THE LIST IS')
            print(lst)
        elif del_dec == 3:
            pos = int(input("ENTER THE POSITION\n=> "))
            lst.pop(pos)
            print(f'GREAT NOW THE LIST IS')
            print(lst)
        else:
            print("WRONG INPUT!")
    else:
        running = False

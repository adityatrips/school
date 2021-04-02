def tell_term(trm):
    fib = ()
    a, b = 0, 1
    while a <= trm:
        a, b = b, a+b
        fib += (b,)
    if trm == 0:
        return 0
    else:
        for fib_term in fib:
            if trm == fib_term:
                return fib.index(trm)+1


trm = int(input("ENTER THE TERM\n=> "))
print(tell_term(trm))

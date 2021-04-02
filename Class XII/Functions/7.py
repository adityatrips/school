from random import randint


def rand(n):
    a = 10 ** (x-1)
    b = 10 ** x
    return randint(a, b)


n = int(input("ENTER A NUMBER\n >> "))
print(rand(n))

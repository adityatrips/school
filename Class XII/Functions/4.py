from random import randint


def cust_rand(st, end):
    return randint(st, end)


for i in range(2):
    print(cust_rand(10, 20))

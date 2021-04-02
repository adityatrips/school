def nth_root(x, n=2):
    return x ** (1/n)


x = float(input("ENTER X\n >> "))
n = float(input("ENTER N\n >> "))

print(nth_root(x, n))

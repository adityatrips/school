term = int(input("ENTER THE TERM\n=> "))
fib = [0, 1, 1]
for i in range(term-2):
    fib = fib + [fib[i+1] + fib[i+2]]
print(fib[term])

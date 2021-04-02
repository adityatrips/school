fib = (0, 1, 1)
for i in range(6):
    fib += (fib[i+1] + fib[i+2],)
print(fib)

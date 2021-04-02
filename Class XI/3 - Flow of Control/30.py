def isPrime(n):
  for i in range(2, n//2):
    if n % i == 0:
      return False
  else:
    return True


def prime_fact(n):
  fact = []
  for i in range(2, n//2):
    if (n % i) == 0:
      fact.append(i)
    else:
      pass
  return fact


n = int(input("ENTER A NUMBER\n=> "))
prime_f = prime_fact(n)
for number in prime_f:
  if isPrime(number):
    print(number, end=' ')

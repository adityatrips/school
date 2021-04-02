n = int(input("ENTER N\n=> "))


def isEven(n):
  if n % 2 == 0:
    return True
  else:
    return False


def isOdd(n):
  if n % 2 == 0:
    return False
  else:
    return True


if isEven(n):
  nbr = []
  for number in range(n+1, 1, -2):
    nbr.append(number)
  print(nbr)

elif isOdd(n):
  nbr = []
  for number in range(n, 1, -2):
    nbr.append(number)
  print(nbr)

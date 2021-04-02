def rev(n):
  return n[::-1]


def isPal(n):
  if n == rev(n):
    return True
  else:
    return False


n = int(input("ENTER A NUMBER\n=> "))

if isPal(n):
  print("Palindrome")
else:
  print("Isn't palindrome")

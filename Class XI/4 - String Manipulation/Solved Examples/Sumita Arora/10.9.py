def reverse(s):
  return s[::-1]


s = input("Enter a string")

if s == reverse(s):
  print("Palindrome")
else:
  print("Not palindrome")

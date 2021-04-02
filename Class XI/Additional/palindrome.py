tnum = num = int(input("Enter a number\n=> "))
reverse = 0
while tnum:
  digit = tnum % 10
  tnum = tnum // 10
  reverse = reverse * 10 + digit
print("Reverse:", reverse)
if reverse == num:
  print("isPalindrome")
else:
  print("isntPalindrome")

s = input("ENTER A STRING\n=> ")
digits = []
sumation = 0

for ch in s:
  if ch == '1' or ch == '2' or ch == '3' or ch == '4' or ch == '5' or ch == '6' or ch == '7' or ch == '8' or ch == '9' or ch == '0':
    ch = int(ch)
    digits.append(ch)
print(f'Original: {s}')
print(f'Digits: {digits}')

for digit in digits:
  sumation += digit

print(f'Sum of digits: {sumation}')

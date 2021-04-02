x = int(input("ENTER A INTEGER\n=> "))
s = input("ENTER A STRING\n=> ")
s_num = []

for char in s:
  if char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9' or char == '0':
    s_num.append(char)

print(f'{x} + {"".join(s_num)} = {x+int("".join(s_num))}')

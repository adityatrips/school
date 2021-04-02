s = input("ENTER A STRING\n=> ").lower()
x = input("ENTER A CHARACTER\n=>").lower()
counter = 0

for letter in s:
  if letter == x:
    counter += 1
print(f'{x} was seen {counter} times!')

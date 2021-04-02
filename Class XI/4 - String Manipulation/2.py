s = input("ENTER A STRING\n=> ").lower()
vowels = ['a', 'e', 'i', 'o', 'u']
for letter in s:
  for vowel in vowels:
    if letter == vowel:
      s = s.replace(letter, '*')
print(s)

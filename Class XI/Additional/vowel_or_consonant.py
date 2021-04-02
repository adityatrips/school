letter = input("Enter a letter")
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
  print("Vowel")
elif letter != 'a' or letter != 'e' or letter != 'i' or letter != 'o' or letter != 'u':
  print("Consonant")
elif len(letter) > 1:
  print("I said a letter only, smarty!")
else:
  print("SmartyPants")

running = True

while running:
  new_str = ''
  s = input("ENTER A SENTENCE, OR [q]UIT\n=> ")
  if s == 'q':
    running = False
  else:
    for i in range(len(s)):
      if s[i].isupper():
        new_str += s[i].lower()
      elif s[i].islower():
        new_str += s[i].upper()
      elif s[i] == ' ':
        new_str += s[i]
  print(new_str)

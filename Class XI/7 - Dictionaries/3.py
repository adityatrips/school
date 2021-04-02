letter_words = {
    0: 'Zero',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
}

n = input("ENTER A NUMBER\n=> ")

word_n = []

for num in n:
  for key, val in letter_words.items():
    if int(num) == key:
      word_n.append(val)

print(' '.join(word_n))

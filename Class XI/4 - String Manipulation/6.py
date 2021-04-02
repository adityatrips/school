sentence = input("ENTER A SENTENCE\n=> ")
sentence_split = sentence.split()
words = 0
characters = 0
per_alphanumeric = 0

print(f'THE GIVEN SENTENCE: {sentence}')

for word in sentence_split:
  words += 1

print(f'Word count: {words}')

for char in sentence:
  characters += 1

print(f'Character count: {characters}')

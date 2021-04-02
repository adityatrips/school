sentence = input("ENTER A SENTENCE\n >> ")
words = len(sentence.split())
chars = len(sentence)
alphanum = 0

for i in sentence:
    if i.isalnum():
        alphanum += 1

print(f'Original Sentence: {sentence}')
print(f'Words            : {words}')
print(f'Characters       : {chars}')
print(f'% alphanumeric   : {(alphanum / chars) * 100}')

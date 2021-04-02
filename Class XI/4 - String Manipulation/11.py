def word_count(s):
    return len(s.split())

s = input("ENTER A SENTENCE\n=> ")
print(f'Word count is {word_count(s)}')
def rm_letter(sentence, lttr):
    words = sentence.split()
    final = []
    for word in words:
        final.append(''.join(word.split(lttr)))
    return ' '.join(final)


sentence = input("ENTER A SENTENCE\n >> ")
lttr = input("ENTER A LETTER\n >> ")
print(rm_letter(sentence, lttr))

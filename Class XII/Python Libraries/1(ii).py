def capword(s):
    words = s.split()
    final = []
    for word in words:
        fst = word[0].upper()
        rst = word[1:]
        fn = f'{fst}{rst}'
        final.append(fn)
    return ' '.join(final)


sentence = input("ENTER A SENTENCE\n >> ")

print(capword(sentence))

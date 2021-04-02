def add_to_word_and_len(key, value):
    word_and_len[key] = value


def get_key(val):
    for key, value in word_and_len.items():
        if val == value:
            return key
    return False


word_and_len = {}

s_lst = eval(input("ENTER A LIST OF STRINGS\n=> "))
if len(s_lst) == 0 or s_lst == '':
    print("Please enter something")
else:
    for string in s_lst:
        add_to_word_and_len(str(string), int(len(string)))
    print(
        f"Longest word: {max(word_and_len, key=word_and_len.get)} and len is {len(max(word_and_len, key=word_and_len.get))}")

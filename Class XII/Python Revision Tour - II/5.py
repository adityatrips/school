def get_key_from_val(d, value):
    for key, val in d.items():
        if val == value:
            return key


words = list(
    map(str, input("ENTER A LIST OF WORDS SEPARATED BY A SPACE\n >> ").split())
)

char_cnt = {}

for word in words:
    char_cnt[word] = len(word)

print(f"Longest word is {get_key_from_val(char_cnt, max(char_cnt.values()))}")

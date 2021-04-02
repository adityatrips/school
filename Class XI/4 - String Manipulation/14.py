def append_to_dict(dictionary, key, value):
    dictionary[key] = value


def get_key(dictionary, val):
    for key, value in dictionary.items():
        if value == val:
            return key
    return "Key not found"


s = input("ENTER A SENTENCE\n=> ").split()
len_dict = {}

for word in s:
    append_to_dict(len_dict, str(word), len(word))

for key, value in len_dict.items():
    value_dict = []
    value_dict.append(value)
    max_val = max(value_dict)
else:
    print(f'{max_val} is the longest word\'s length, the word is {get_key(len_dict, max_val)}')

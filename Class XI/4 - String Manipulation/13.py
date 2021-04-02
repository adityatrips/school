vowel = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0

s = input("ENTER A STRING\n=> ")
for ch in s:
    if ch in vowel:
        vowel_count += 1
print(f'Vowel count is {vowel_count}')

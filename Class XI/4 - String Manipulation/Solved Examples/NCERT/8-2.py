def vowel_replace(st):
    vowel = 'aeiouAEIOU'
    st_new = []
    for ch in st:
        if ch in vowel:
            st_new.append('*')
        else:
            st_new.append(ch)
    return st_new


st = input("ENTER STRING\n=> ")
st_new = vowel_replace(st)
print(f'Original: {st}')
print(f'Modified: {"".join(st_new)}')

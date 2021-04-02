def count_ch(ch, st):
    count = 0
    for char in st:
        if char == ch:
            count += 1
    return count


st = input("ENTER A STRING\n=> ")
ch = input("ENTER A CHARACTER\n=> ")
count_of_ch = count_ch(ch, st)
print(f'{ch} occured {count_of_ch} in {st} times')

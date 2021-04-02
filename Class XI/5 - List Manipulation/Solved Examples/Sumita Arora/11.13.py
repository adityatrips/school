lst = eval(input("Enter a list\n=> "))
uniq = []
dupl = []
count = 0
d = {}
dupl_res = []


def add(key, value):
    d[key] = value


for index, el in enumerate(lst):
    if lst.count(el) == 1:
        uniq.append(el)
    else:
        dupl.append(el)

for el in lst:
    add(el, lst.count(el))

print('Unique elements:', uniq)
for i in lst:
    if i not in dupl_res:
        dupl_res.append(i)
print('Duplicate elements:', dupl_res)
for el, cnt in d.items():
    print(f'{el} occurs {cnt} times')

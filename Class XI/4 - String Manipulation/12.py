s = input("ENTER A SENTENCE WITH PARENTHESES\n=> ")
start = 0
end = 0
for ch in s:
    if ch == "(":
        start += 1
    elif ch == ')':
        end += 1
if start == end:
    print("Brackets matched")
else:
    print("Bracket are not matching")

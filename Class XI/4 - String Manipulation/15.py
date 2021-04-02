def rev(s):
    return s[::-1]


s = input("ENTER A LINE\n=> ").split()
for word in s:
    print(rev(word))

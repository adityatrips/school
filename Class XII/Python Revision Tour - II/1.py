phone = input("ENTER PHONE NUMBER (XXX-XXX-XXXX)\n >> ")
if phone[3] == phone[-5] == '-':
    print("Valid")
else:
    print("Invalid")

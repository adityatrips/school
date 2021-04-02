ph_no = input("ENTER A PHONE NUMBER (XXX-XXX-XXXX)\n=> ")
if ph_no[3] == '-' and ph_no[-5] == '-' and len(ph_no) == 12:
  print('Phone number is valid!')
else:
  print('Phone number isn\'t valid!')

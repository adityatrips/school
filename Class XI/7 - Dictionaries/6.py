def add2dict(d, k, val):
  d[k] = val


alphabetical_order = []
m = {
    'JANUARY': 31,
    'FEBRUARY': 28,
    'MARCH': 31,
    'APRIL': 30,
    'MAY': 31,
    'JUNE': 30,
    'JULY': 31,
    'AUGUST': 31,
    'SEPTEMBER': 30,
    'OCTOBER': 31,
    'NOVEMBER': 30,
    'DECEMBER': 31,
}
print('1: ENTER A MONTH AND GET THE DAYS')
print('2: PRINT ALL MONTHS IN ALPHABETICAL ORDER')
print('3: PRINT ALL MONTHS WITH 30 DAYS')
print('4: PRINT (KEY, VALUE) PAIR SORTED BY NUMBER OF DAYS')
dec = int(input("ENTER YOUR DECISION\n=> "))
if dec == 1:
  m_name = input("ENTER A MONTH NAME\n=> ").upper()
  print(f'NUMBER OF DAYS IN {m_name} IS {m[m_name]}')
elif dec == 2:
  alphabetical_order = [months.lower() for months in m.keys()]
  alphabetical_order.sort()
  print(alphabetical_order)
elif dec == 3:
  for key, val in m.items():
    if val == 30:
      print(key)
else:
  numerical_order = sorted([days for days in m.values()])
  print(numerical_order)

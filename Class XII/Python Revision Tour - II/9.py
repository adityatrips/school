def get_key_from_val(d, value):
    for key, val in d.items():
        if val == value:
            return key


months = {
    'january': 31,
    'february': 28,
    'march': 31,
    'april': 30,
    'may': 31,
    'june': 30,
    'july': 31,
    'august': 31,
    'september': 30,
    'october': 31,
    'november': 30,
    'december': 31,
}
m = input("ENTER A MONTH\n >> ").lower()
print(f'{m} has {months[m]}')

print(sorted(months.keys()))

for key, val in months.items():
    if val == 31:
        print(key, 'has 31 days')

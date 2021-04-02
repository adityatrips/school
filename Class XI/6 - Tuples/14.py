import statistics

int_tuple = eval(input("ENTER A TUPLE OF NUMERIC VALUES\n=> "))
mean = sum(int_tuple)/len(int_tuple)
print(f'Mean is {mean}')
print(f'Module mean: {statistics.mean(int_tuple)}')

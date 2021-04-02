def avg(n):
  sum_n = 0
  for i in n:
    sum_n += i
  return sum_n / len(n)


n = list(map(float, input("ENTER NUMBERS SEPARATED BY A SPACE\n=> ").split()))

print(avg(n))

from random import randint

arr = []
mean = 0
median = 0
mode = 0
sum_for_mean = 0
occurence = 0

for _ in range(6):
  arr.append(randint(1, 100))

print("The generated array is", arr)

for i in arr:
  sum_for_mean += i

mean = sum_for_mean / 6
print(f"Mean is {mean}")

for i in arr:
  arr.sort()
  median = (arr[2] + arr[-2]) / 2
print(f"Median is {median}")

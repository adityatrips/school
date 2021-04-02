t = ((1, 2), (3, 4.15, 5.15), (7, 8, 12, 15))
m1 = sum(t[0])/len(t[0])
print("Mean element 0:", m1)
m2 = sum(t[1])/len(t[1])
print("Mean element 1:", m2)
m3 = sum(t[2])/len(t[2])
print("Mean element 2:", m3)
mean_of_means = (m1+m2+m3)/3
print("Mean of means:", mean_of_means)

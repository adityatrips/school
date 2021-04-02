def linspace(a, b):
    d = int((b-a)/3)
    return [a, a+d, a+(2*d), b]


fst = int(input("ENTER A NUMBER\n >> "))
snd = int(input("ENTER A NUMBER\n >> "))
nums = linspace(fst, snd)

print(nums[0], nums[1], nums[2], nums[3])

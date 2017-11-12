import math

day = input()

d = 0
if day == "Monday":
    d = 0
elif day == "Tuesday":
    d = 1
elif day == "Wednesday":
    d = 2
elif day == "Thursday":
    d = 3
elif day == "Friday":
    d = 4
elif day == "Saturday":
    d = 5
else:
    d = 6

a = int(input())
i = math.floor(a / 7)
modulo = a % 7

li = [i, i, i, i, i, i, i]
for l in range(0, modulo):
    li[l + d % 7] += 1


print(' '.join(map(str, li)))

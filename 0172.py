n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.append(0)

power = []
for x in range(0, n):
    power.append(k)

for i in range(0, len(a)):
    power[0] -= a[i]
    if power[0] <= 0:
        power[1] += power[0]
        del power[0]

used = 0
for x in range(0, len(power)):
    if power[x] <= 0:
        power[x + 1] += power[x]
    if power[x] != k:
        used -= 1
    used += 1

print(used)

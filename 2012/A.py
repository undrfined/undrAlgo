import sys

k = list(map(int, input().split()))
d = sorted(list(map(int, input().split())))

for i in range(0, len(d)):
    k[0] -= d[i]
    if k[0] < 0:
        print(i)
        sys.exit()

print(k[1])

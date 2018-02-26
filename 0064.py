from math import floor

maxn = 1000005
inf = 10000000000000000

d = {}
t = int(input())

for i in range(2, maxn):
    j = 2
    while i * j < maxn:
        d.setdefault(i * j, []).append(i)
        j += 1

for i in range(1, maxn):
    d.setdefault(i, []).append(i)

for i in range(0, t):
    n, m = map(int, input().split())
    if n > m:
        m, n = n, m
    if n == 1:
        print(floor(m / d[m][0]))
    else:
        best = inf
        for x in range(0, len(d[n])):
            for y in range(0, len(d[m])):
                a, b = d[n][x], d[n][y]
                if a > 3:
                    best = min(best, a)
                if b > 3:
                    best = min(best, b)
                if a * b > 3:
                    best = min(best, a * b)
        if best == inf:
            print(1)
        else:
            print(floor(n * m / best))

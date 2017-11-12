n = int(input())
a = 0
d = list(map(int, input().split()))
for i in range(0, n):
    a += d[i] - 1

print(a)

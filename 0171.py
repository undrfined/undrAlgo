from math import sqrt

a = 0
n = int(input())
for i in range(0, n):
    b = list(map(int, input().split()))
    a += sqrt(abs(b[0] - b[2]) ** 2 + abs(b[1] - b[3]) ** 2)

print(int(a))

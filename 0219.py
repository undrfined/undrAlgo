from math import pi

r, h = map(int, input().split())

v = (4 / 3) * pi * (r ** 3)
v2 = pi * (r ** 2) * (h - 2 * r)

print(v + v2)

s = 4 * pi * (r ** 2)
s2 = 2 * pi * r * (h - 2 * r)
print(s + s2)

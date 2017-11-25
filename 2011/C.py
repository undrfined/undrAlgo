from math import sqrt

a, b = map(int, input().split())

d = str(round(sqrt(a ** 2 + b ** 2), 2))
if len(d.split(".")) == 1:  # lol
    d += ".00"
elif len(d.split(".")[1]) != 2:
    d += "0"
print(d)

a, b = map(int, input().split())
mult = a * b

if mult == 0:
    print(0)
else:
    print(1 / (a * b))

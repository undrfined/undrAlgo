a, b, c, d = map(int, input().split())
li = []
all = ((b - a + 1) * (d - c + 1))


def factors(num, d=2):
    while num > 1:
        n1, n2 = divmod(num, d)
        if n2:
            d += 1
        else:
            yield d
            num = n1


def gcd(a: int, b: int)->int:
    if b == 0:
        return a
    return gcd(b, a % b)


for u in range(0, int(input())):
    num = int(input())
    p = 0
    f = list(factors(num))
    la = set()
    for i in range(0, len(f)):
        for i2 in range(0, len(f)):
            if i2 == i:
                continue
            t = f[i2] * f[i]
            la.add(t)
    la = list(la)
    for i in range(0, len(la)):
        t = la[i]
        t2 = int(all / t)
        if a <= t <= b or c <= t <= d:
            p += 1
    """if a * c <= num <= b * d:
        for x in range(a, b + 1):
            for y in range(c, d + 1):
                if x * y == num:
                    p += 1
    """
    li.append(p)

for i in range(0, len(li)):
    g = gcd(li[i], ((b - a + 1) * (d - c + 1)))
    print("{p}/{q}".format(p=int(li[i] / g), q=int(all / g)))

n = int(input())
li = []

for u in range(0, n):
    li.append(list(map(int, input().split())))

for u in range(0, n):
    x = li[u][0]
    y = li[u][1]
    seen = 0
    for u2 in range(0, n):
        if u == u2:
            continue
        x2 = li[u2][0]
        y2 = li[u2][1]
        a = (y - y2, x2 - x)
        v = x * y2 - x2 * y
        bad = False
        for u3 in range(0, n):
            if u3 == u2 or u3 == u:
                continue
            x3 = li[u3][0]
            y3 = li[u3][1]
            if not (min(x2, x) <= x3 <= max(x2, x)) or not (min(y2, y) <= y3 <= max(y2, y)):
                continue
            if a[0] * x3 + a[1] * y3 + v == 0:
                bad = True
                break
        if not bad:
            seen += 1
    print(seen + 1)

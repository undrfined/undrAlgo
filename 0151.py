from math import sqrt


n = int(input())
data = list(input())
c = int(sqrt(n))
li = {}

i = 0
for x in range(0, c):
    li[x] = {}
    for y in range(0, c):
        li[x][y] = data[i]
        i += 1


def diag(li: dict, d: int)->list:
    x = d + 1
    y = 0
    s = []
    if d >= len(li):
        x = len(li) - 1
        y = d - len(li)
        while y != len(li) - 1:
            y += 1
            s.append(li[x][y])
            x -= 1
    else:
        while x != 0:
            x -= 1
            s.append(li[x][y])
            y += 1
    return list(reversed(s))


st = []
for d in range(0, n):
    ls = diag(li, d)
    if ls == []:
        break
    for i2 in range(0, len(ls)):
        st.append(str(ls[i2]))

print(''.join(st))

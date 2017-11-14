import sys

data = input().split()
x, y = map(int, data)
ls = {}
ls[x] = {}
ls[x][y] = 1

s = list(input())

for i in range(0, len(s)):
    a = s[i]
    if a == 'R':
        x += 1
    elif a == 'L':
        x -= 1
    elif a == 'U':
        y += 1
    else:
        y -= 1
    if ls.get(x) is None:
        ls[x] = {}
    if ls.get(x).get(y) is None:
        ls[x][y] = 1
    else:
        print("Fail")
        print(i + 1)
        sys.exit()

print("Success")

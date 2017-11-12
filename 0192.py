import sys

data = input().split()
x, y = map(int, data)
ls = []

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
    if (x, y) in ls:
        print("Fail")
        print(i + 1)
        sys.exit()
    ls.append((x, y))

print("Success")

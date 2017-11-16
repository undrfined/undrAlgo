s = list(input())
a = 0
for i in range(0, len(s)):
    if s[i] == '4' or s[i] == '7':
        a += 1

print(str(a))

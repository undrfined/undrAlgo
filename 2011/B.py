n, k, z = map(int, input().split())
li = sorted(list(map(int, input().split())))
i = 0

while len(li) > 0 and z >= (li[0] * 2) and k > 0:
    i += 1
    z -= li[0] * 2
    k -= 1
    del li[0]

print(i)

n = int(input())

li = []
while True:
    a = tuple(map(int, input().split()))
    if a[0] == 0 and a[1] == 0:
        break
    li.append(a)
li2 = list()


def check(to_delete: list, li: list, li2: list, i: int):
    added = False
    for i2 in range(0, len(li)):
        if li[i2] == li[i] or li[i2] in to_delete:
            continue
        a = li[i2][0]
        b = li[i2][1]
        if a in li2[length] or b in li2[length]:
            li2[length].append(a)
            li2[length].append(b)
            to_delete.append(li[i2])
            added = True
    if added:
        check(to_delete, li, li2, i)


to_delete = list()

for i in range(0, len(li)):
    if li[i] in to_delete:
        continue
    li2.append([])
    length = len(li2) - 1
    li2[length].append(li[i][0])
    li2[length].append(li[i][1])
    to_delete.append(li[i])
    check(to_delete, li, li2, i)
    li2[length] = list(set(li2[length]))

print(str(len(li2) - 1))

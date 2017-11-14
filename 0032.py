"""
Let's take this for example.
6
1 2
2 3
3 4
4 2
6 7
7 8

We have one ended cycle (2-4) and one not ended
"""

n = int(input())
li = []

for i in range(0, n):
    li.append(list(map(int, input().split())))


def find(li2: list, what: list)->list:
    for x in range(0, len(li2)):
        if what[1] == li2[x][0]:
            yield x
    return None


def finds(test: list, li2: list, num: list):
    branch = list(li2)
    found = list(find(branch, num))
    print("Found " + str(found))
    for a in range(0, len(found)):
        temp = branch[found[a]]
        del branch[found[a]]
        print("DELETE at " + str(found[a]) + ": " + str(branch))
        print("Trying to find " + str(temp))
        yield finds(test, branch, temp)
    return "Ended. " + str(found)


# for i in range(0, len(li)):
i = 0
current = li[i]
test = []
del li[i]
print(li)
print("START " + ', '.join(map(str, current)))
print(map(list, map(list, list(finds(test, li, current)))))
# found = list(find(li, current))
# print(found)
# finds(li, current[1])

"""real_list = list(set(real_list))
print(len(real_list))
print(' '.join(map(str, sorted(real_list))))
"""

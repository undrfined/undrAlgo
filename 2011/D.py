n = 11  # int(input())
st = """41 67 34 0 69 24 78 58 62 64 5
45 81 27 61 91 95 42 27 36 91 4
2 53 92 82 21 16 18 95 47 26 71
38 69 12 67 99 35 94 3 11 22 33
73 64 41 11 53 68 47 44 62 57 37
59 23 41 29 78 16 35 90 42 88 6
40 42 64 48 46 5 90 29 70 50 6
1 93 48 29 23 84 54 56 40 66 76
31 8 44 39 26 23 37 38 18 82 29
41 33 15 39 58 4 30 77 6 73 86
21 45 24 72 70 29 77 73 97 12 86
"""
li = {}
for y in range(0, n):
    t = list(map(int, st.split("\n")[y].split()))
    li[y] = {}
    for x in range(0, 11):
        li[y][x] = t[x]

best = {}
for y in li:
    a = li[y]
    mx = max(a.values())
    print("Player #{}, max = {}".format(y, mx))
    p = None
    for i in a:
        if a[i] == mx:
            print("Found! " + str(i))
            p = i
            break
    best[y] = (p, mx)

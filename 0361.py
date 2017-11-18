from sys import exit


data = input().split()
n, k = list(map(int, data))

sweets = sorted(list(map(int, input().split())))

last = sweets[0]
have = 1

for i in range(1, len(sweets)):
    if sweets[i] == last:
        have += 1
        if have >= k:
            print(' '.join(map(str, sweets)))
            exit()
    else:
        have = 0

print("Oh sh*t")

n = int(input())
data = list(input())
current = (0, 0)
total = (0, 0)
for i in range(0, n):
    kolya = data[i] == 'K'
    current = (current[0] + (1 if kolya else 0), current[1] + (1 if not kolya else 0))
    if current[0] >= 11 or current[1] >= 11:
        if abs(current[0] - current[1]) >= 2:
            total = (total[0] + (1 if kolya else 0), total[1] + (1 if not kolya else 0))
            current = (0, 0)

print(*total, sep=':')
if current != (0, 0):
    print(*current, sep=':')

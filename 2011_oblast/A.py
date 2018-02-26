cost = int(input())
total = 500
c = 0

while total != cost:
    c += 1
    if total - 500 >= cost:
        total -= 500
    elif total - 200 >= cost:
        total -= 200
    elif total - 100 >= cost:
        total -= 100
    elif total - 50 >= cost:
        total -= 50
    elif total - 20 >= cost:
        total -= 20
    elif total - 10 >= cost:
        total -= 10
    elif total - 5 >= cost:
        total -= 5
    elif total - 2 >= cost:
        total -= 2
    else:
        total -= 1

print(c)

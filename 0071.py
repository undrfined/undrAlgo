data = list(input())
li = []
for i in range(0, len(data)):
    if data[i] == "(" or data[i] == ")":
        li.append((i, data[i]))
print(int(len(li) / 2))

i = 0
while len(li) > 0:
    if li[i][1] == ")":
        num = li[i - 1][0] + 1
        num2 = li[i][0] + 1
        del li[i]
        del li[i - 1]
        print(num, num2)
        i -= 2
    i += 1

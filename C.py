s = list(input())
s_real = list(s)
from_start = True
from_number = 0

for i in range(0, len(s)):
    s[i] = s_real[from_number if from_start else (-from_number - 1)]
    from_start = not from_start
    if from_start:
        from_number += 1

print("".join(s))

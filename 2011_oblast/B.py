from math import floor
from math import pow

a, b = map(int, input().split())
fr = a
to = b
for i in range(a, a + 10):
    if "6" in str(i):
        fr = i
        break

while "6" not in str(to):
    to -= 1

print(floor(to / 10))

import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import Counter


n = int(input())

d = Counter()

for _ in range(n):
    s, x = input().split()

    d[s] += int(x)

if 5 in d.values():
    print("YES")
else:
    print("NO")

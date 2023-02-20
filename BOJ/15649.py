import sys; input = lambda: sys.stdin.readline().rstrip()
from itertools import permutations


n, m = map(int, input().split())

for i in permutations(range(1, n + 1), m):
    print(*i)

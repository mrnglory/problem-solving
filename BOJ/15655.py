import sys; input = lambda: sys.stdin.readline().rstrip()
from itertools import combinations


n, m = map(int, input().split())
nums = map(int, input().split())

for i in list(combinations(sorted(nums), m)):
    print(*sorted(i))

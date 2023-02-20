import sys; input = lambda: sys.stdin.readline().rstrip()
from itertools import permutations


n, m = map(int, input().split())
nums = list(map(int, input().split()))

result = []

for i in permutations(nums, m):
    result.append(i)

for i in sorted(result):
    print(*i)

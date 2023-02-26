import sys; input = lambda: sys.stdin.readline().rstrip()
from itertools import combinations


n, s = map(int, input().split())
nums = list(map(int, input().split()))

count = 0

for i in range(n + 1):
    for case in combinations(nums, i):
        if case and s == sum(case):
            count += 1

print(count)

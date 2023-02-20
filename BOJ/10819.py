import sys; input = lambda: sys.stdin.readline().rstrip()
from itertools import permutations


n = int(input())
nums = list(map(int, input().split()))

cases = [list(i) for i in permutations(nums, n)]

sums = []

for i in range(len(cases)):
    s = 0
    case = cases[i]

    for j in range(n):
        try:
            s += abs(case[j] - case[j + 1])
        except IndexError:
            break

    sums.append(s)

print(max(sums))

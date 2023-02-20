from sys import stdin

n, m = map(int, input().split())

result = "Yes"

for _ in range(2 * m):
    k = list(map(int, stdin.readline().rstrip().split()))

    if k != sorted(k, reverse=True):
        result = "No"
        break

print(result)

n = int(input())
p = sorted([*map(int, input().split())])

answer = 0

for i in range(1, n + 1):
    answer += sum(p[0:i])

print(answer)

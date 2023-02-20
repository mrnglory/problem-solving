import sys; input = lambda: sys.stdin.readline().rstrip()


n = int(input())
meets = set()
meets.add("ChongChong")

for _ in range(n):
    a, b = input().split()

    if a in meets:
        meets.add(b)
    elif b in meets:
        meets.add(a)

print(len(meets))

import sys; input = lambda: sys.stdin.readline().rstrip()


len1, len2 = map(int, input().split())

a = set([input() for _ in range(len1)])
b = set([input() for _ in range(len2)])

result = a & b

print(len(result))
print(*sorted(result), sep="\n")

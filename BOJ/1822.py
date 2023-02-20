import sys; input = lambda: sys.stdin.readline().rstrip()


len1, len2 = map(int, input().split())

a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

result = a - b

print(len(result))

if len(result):
    print(*sorted(result))

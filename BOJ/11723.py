import sys; input = lambda: sys.stdin.readline().rstrip()

m = int(input())

s = set()

for _ in range(m):
    a = list(input().split())

    if a[0] not in ("all", "empty"):
        x = int(a[1])
        a = a[0]

        if a == "add":
            s.add(x)
        elif a == "remove":
            s.discard(x)
        elif a == "check":
            if x in s:
                print(1)
            else:
                print(0)
        elif a == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)
    else:
        a = a[0]

        if a == "all":
            s = set([i for i in range(1, 20 + 1)])
        elif a == "empty":
            s.clear()
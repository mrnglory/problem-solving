import sys; input = lambda: sys.stdin.readline().rstrip()


n = int(input())
gomgom = set()
count = 0

for _ in range(n):
    item = input()

    if item != "ENTER":
        if item not in gomgom:
            gomgom.add(item)
            count += 1

    else:
        gomgom.clear()

print(count)

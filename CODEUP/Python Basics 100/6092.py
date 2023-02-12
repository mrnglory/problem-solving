n = int(input())
numbers = map(int, input().split())

called = dict.fromkeys(range(1, 23 + 1), 0)

for number in [*numbers]:
    called[number] += 1

print(*called.values())

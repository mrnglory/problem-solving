baskets = [list(map(int, input().split())) for _ in range(2)]

answer = 0
a, b = baskets[0]
c, d = baskets[1]

print(min(a + d, b + c))

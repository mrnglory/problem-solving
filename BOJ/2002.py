import sys; input = lambda: sys.stdin.readline().rstrip()


n = int(input())

car_in = {k: v for v, k in enumerate([input() for _ in range(n)])}
car_out = [input() for _ in range(n)]

count = 0

for i in range(n):
    for j in range(i + 1, n):
        if car_in[car_out[i]] > car_in[car_out[j]]:
            count += 1
            break

print(count)

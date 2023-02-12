n = int(input())
numbers = map(int, input().split())

print(*[*numbers][::-1])

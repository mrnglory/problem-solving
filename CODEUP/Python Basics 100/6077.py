number = int(input())

answer = 0

for i in range(number + 1):
    if i % 2 == 0:
        answer += i

print(answer)

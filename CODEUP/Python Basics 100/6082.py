number = int(input())

i = 1
answer = ""

while True:
    if (i % 10 or i // 10) in (3, 6, 9):
        answer += "X "
    else:
        answer += f"{i} "
    
    i += 1
    
    if i > number:
        break

print(answer.rstrip(" "))

number = int(input())

sum = i = 0

while True:
    i += 1
    sum += i
    
    if sum >= number:
        print(i)
        break

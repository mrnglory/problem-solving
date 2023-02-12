a, m, d, n = map(int, input().split())

number = a
i = 1

while True:
    if i == n:
        print(number)
        break
    
    number = number * m + d

    i += 1

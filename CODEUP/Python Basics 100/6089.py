a, r, n = map(int, input().split())

i = 1

while True:
    number = a * r ** (i - 1)
    
    if i == n:
        print(number)
        break
    
    i += 1

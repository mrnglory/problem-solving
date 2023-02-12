a, d, n = map(int, input().split())

i = 1

while True:
    number = a + (i - 1) * d
    
    if i == n:
        print(number)
        break
    
    i += 1
    
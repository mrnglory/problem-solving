a, b, c = map(int, input().split())

numbers = [a, b, c]

for number in numbers:
    if number % 2 == 0:
        print(number)

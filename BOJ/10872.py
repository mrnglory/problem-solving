import sys; input = lambda: sys.stdin.readline().rstrip()


n = int(input())

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(n))

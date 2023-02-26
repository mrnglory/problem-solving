import sys; input = lambda: sys.stdin.readline().rstrip()


n = int(input())

results = []

for _ in range(n):
    rhymes = set()
    count = 0
    counter = {}

    n, l, f = map(int, input().split())
    words = list(input().split())

    for word in words:
        rhymes.add(word[l-f:])

    for word in words:
        c = 0
        if word[l-f:] in rhymes:
            c += 1
        counter[word] = c

    print(counter)





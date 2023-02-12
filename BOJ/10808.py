import string

word = input()

alphabets = dict.fromkeys(string.ascii_lowercase, 0)
for c in word:
    alphabets[c] += 1

print(*list(alphabets.values()))

import sys; input = lambda: sys.stdin.readline().rstrip()


def is_palindrome(s: str, l: int, r: int) -> int:
    global count
    count += 1

    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return is_palindrome(s, l+1, r-1)


t = int(input())

for _ in range(t):
    word = input()
    count = 0
    print(is_palindrome(s=word, l=0, r=len(word)-1), count)

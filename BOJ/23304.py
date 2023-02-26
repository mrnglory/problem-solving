import sys; input = lambda: sys.stdin.readline().rstrip()


def is_palindrome(s: str) -> bool:
    length = len(s)

    if length == 1:
        return True

    left = s[:length//2]
    right = s[length//2 if length % 2 == 0 else length//2+1:]

    if left != right:
        return False

    if is_palindrome(s=left) & is_palindrome(s=right):
        return True

    return False


word = input()

if is_palindrome(s=word):
    print("AKARAKA")
else:
    print("IPSELENTI")

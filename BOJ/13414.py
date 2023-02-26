import sys; input = lambda: sys.stdin.readline().rstrip()


k, l = map(int, input().split())

s = {}
for i in range(l):
    student = input()

    if student in s.keys():
        del s[student]

    s[student] = i

result = list(s.keys())

for student in result[0:k]:
    print(student)

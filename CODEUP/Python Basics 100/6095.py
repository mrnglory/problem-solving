n = int(input())
indexes = [[*map(int, input().split())] for _ in range(n)]

board = [[0 for _ in range(19)] for _ in range(19)]

for index in indexes:
    x, y = index[0], index[1]
    board[x - 1][y - 1] = 1

for row in board:
    print(*row)

board = [[*map(int, input().split())] for _ in range(19)]

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    
    for j in range(19):
        if board[x][j] == 0:
            board[x][j] = 1
        else:
            board[x][j] = 0
            
        if board[j][y] == 0:
            board[j][y] = 1
        else:
            board[j][y] = 0

for row in board:
    print(*row)

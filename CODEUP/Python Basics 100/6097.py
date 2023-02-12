h, w = map(int, input().split())

board = [[0 for _ in range(w)] for _ in range(h)]

n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    
    x -= 1
    y -= 1
    
    for j in range(l):
        if d == 0:
            board[x][y+j] = 1
            
        elif d == 1:
            board[x+j][y] = 1

for row in board:
    print(*row)

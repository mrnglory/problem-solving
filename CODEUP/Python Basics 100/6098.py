maze = [[*map(int, input().split())] for _ in range(10)]

x = y = 1

while True:
    try:
        if maze[x][y] == 1:
            x += 1
            y -= 1
        
        if maze[x][y] == 0:
            maze[x][y] = 9
            y += 1

        if maze[x][y] == 2:
            maze[x][y] = 9
            break
    except IndexError:
        break

for row in maze:
    print(*row)

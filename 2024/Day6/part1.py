with open('input.txt', 'r') as file:
    grid = [list(i[:-1] if i[-1] == '\n' else i) for i in file]
    n, m = len(grid), len(grid[0])
    
    res = 0
    dirs = [-1, 0, 1, 0, -1] # up, right, down, left
    x, y, dir = 0, 0, 0
    for i in range(n):
        if '^' in grid[i]:
            x = i
            y = grid[i].index('^')

    while x >= 0 and y >= 0 and x < n and y < m:
        if grid[x][y] != 'X':
            res += 1
        grid[x][y] = 'X'
        nextX, nextY = x + dirs[dir], y + dirs[dir + 1]
        if grid[nextX][nextY] == '#':
            dir = (dir + 1) % 4
        else:
            x, y = nextX, nextY
    print(res)

import numpy as np
dir = [1, 0, -1, 0, 1]

def BFS(grid, x, y, c, vis):
    if vis[x][y] == 1:
        return 0, 0
    vis[x][y] = 1
    perimeter, area = 0,1
    def IsInRegion(a, b):
        return a >= 0 and b >= 0 and a < len(grid) and b < len(grid[0]) and grid[a][b] == c
    for i in range(4):
        if IsInRegion(x + dir[i], y + dir[i + 1]):
            # how to do this better?
            res = BFS(grid, x + dir[i], y + dir[i + 1], c, vis)
            perimeter += res[0]
            area += res[1]
        else:
            perimeter += 1
    return perimeter, area



with open('input.txt', 'r') as file:
    grid = [list(i) for i in file.read().split('\n')]

    n, m = len(grid), len(grid[0])
    vis = np.zeros([n, m])
    res = 0

    for i in range(n):
        for j in range(m):
            if vis[i][j] != 1:
                vals = BFS(grid, i, j, grid[i][j], vis)
                res += vals[0] * vals[1]

    print(res)
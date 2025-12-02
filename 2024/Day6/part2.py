
import numpy as np
import copy
dirs = [-1, 0, 1, 0, -1] # up, right, down, left
n, m = 0, 0

def InBounds(x, y, n, m):
    return x >= 0 and y >= 0 and x < n and y < m
def SimulatePosition(grid, x, y, dir):
    vis = np.zeros([n,m,4]).tolist()
    while InBounds(x, y, n, m):
        nextX, nextY = x + dirs[dir], y + dirs[dir + 1]
        if not InBounds(nextX, nextY, n, m):
            return False
        if vis[x][y][dir]:
            return True
        vis[x][y][dir] = True
        

        if grid[nextX][nextY] == '#':
            dir = (dir + 1) % 4
        else:
            x, y = nextX, nextY
    return False

print("COPY")
osp = copy.deepcopy(np.zeros([n,m,4]).tolist())
print("COPY2")

with open('input.txt', 'r') as file:
    grid = [list(i[:-1] if i[-1] == '\n' else i) for i in file]
    n, m = len(grid), len(grid[0])
    
    res = 0
    x, y, dir = 0, 0, 0
    for i in range(n):
        if '^' in grid[i]:
            x = i
            y = grid[i].index('^')
    print(x, y)
    # [i[:] for i in grid]
    done = np.zeros([n,m]).tolist()
    vis = np.zeros([n,m,4]).tolist()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#' or grid[i][j] == '^':
                continue
            grid[i][j] = '#'
            res += 1 if SimulatePosition(grid, x, y, dir) else 0
            grid[i][j] = '.'

    print(res)

import numpy as np

def BFS(grid, x, y, prev, vis):
    if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]):
        return 0
    if grid[x][y] != prev + 1:
        return 0
    if grid[x][y] == 9:
        val = int(1 - vis[x][y])
        vis[x][y] = 1
        return val
    cur = grid[x][y]
    # print(prev, cur)
    return BFS(grid, x - 1, y, cur, vis) + BFS(grid, x + 1, y, cur, vis) + BFS(grid, x, y + 1, cur, vis) + BFS(grid, x, y - 1, cur, vis) 

with open('input.txt', 'r') as file:
    grid = [list(map(int, i.strip())) for i in file]
    res = 0
    n, m = len(grid), len(grid[0])
    print(grid, n, m)
    for i in range(n):
        for j in range(m):
            print(i, j, grid[i][j])
            if grid[i][j] == 0:
                print("FOUND", i, j)
                res += BFS(grid, i, j, -1, np.zeros([n,m]))
                print(BFS(grid, i, j, -1, np.zeros([n,m])))
    print(res)
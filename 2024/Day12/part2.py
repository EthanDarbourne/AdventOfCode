import numpy as np
from collections import defaultdict

dir = [1, 0, -1, 0, 1]
side_dirs = [16,8,4,2] # 16 means wall on the bottom, need to travel y - 1 and y + 1 to find same 
dir2 = [0, 1, 0, 1, 0]
# side_dirs = [2, 1]


def BFS(grid, x, y, c, vis, sides):
    if vis[x][y] == 1:
        return 0, 0
    vis[x][y] = 1
    perimeter, area = 0,1
    def IsInRegion(a, b):
        return a >= 0 and b >= 0 and a < len(grid) and b < len(grid[0]) and grid[a][b] == c
    for i in range(4):
        newX, newY = x + dir[i], y + dir[i + 1]
        if IsInRegion(newX, newY):
            # how to do this better?
            res = BFS(grid, newX, newY, c, vis, sides)
            perimeter += res[0]
            area += res[1]
        else:
            sides[(x, y)] += side_dirs[i]
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
                sides = defaultdict(int)
                vals = BFS(grid, i, j, grid[i][j], vis, sides)
                side_count = 0
                # print(sides)
                sides_iter = dict.fromkeys(sides)
                for side in sides_iter:
                    
                    if sides[side] == 0:
                        continue
                    for d in range(4):
                        # print(side, sides[side], side_dirs[d], dir[d], dir[d+1])
                        if sides[side] >= side_dirs[d]: # have fence on this side
                            side_count += 1
                            sides[side] -= side_dirs[d]
                            k = 1
                            # check perpendicular to where we have wall

                            while sides[(side[0] + dir2[d] * k, side[1] + dir2[d + 1] * k)] & side_dirs[d] == side_dirs[d]:
                                sides[(side[0] + dir2[d] * k, side[1] + dir2[d + 1] * k)] -= side_dirs[d]
                                k += 1
                            k = -1
                            while sides[(side[0] + dir2[d] * k, side[1] + dir2[d + 1] * k)] & side_dirs[d] == side_dirs[d]:
                                sides[(side[0] + dir2[d] * k, side[1] + dir2[d + 1] * k)] -= side_dirs[d]
                                k -= 1
                    # print(sides)

                # print(side_count, vals[1], side_count * vals[1])
                res += side_count * vals[1]

    print(res)
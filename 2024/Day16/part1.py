from queue import PriorityQueue
import numpy as np

NOT_FOUND = 1e90 + 7
dirs = [1, 0, -1, 0, 1] # east, north, west, south
def BFS(grid, x, y, dir, vis, targetX, targetY):
    if vis[x][y][dir] == 1:
        return NOT_FOUND
    grid[x][y][dir] = 1
    if x == targetX and y == targetY:
        return 0
    val = NOT_FOUND
    for dir in dirs:
        val = min(val, BFS(grid, x, y))
    


with open("input.txt", "r") as file:

    grid = [list(line) for line in file.read().splitlines()]
    endX, endY, startX, startY = -1,-1,-1,-1
    n,m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'E':
                endY, endX = i, j
            elif grid[i][j] == 'S':
                startY, startX = i, j

    vis = np.zeros([n,m,4])
    q = PriorityQueue()
    for i in range(4):
        if grid[startY + dirs[i + 1]][startX + dirs[i]] == '.':
            q.put((0, (startY, startX, i)))
    iters = 0

    valid = ['.', 'E']
    def GetTurns(a, b): # 0,1,2,3
        if abs(b - a) == 2:
            return 2000
        if a == b:
            return 0
        return 1000
    best_points = NOT_FOUND
    while not q.empty():
        points, data = q.get()
        y, x, dir = data
        if vis[y][x][dir] == 1:
            continue
        vis[y][x][dir] = 1
        if endY == y and endX == x:
            print("found end 2")
            best_points = points
            break
        iters += 1
        for i in range(4):
            if grid[y + dirs[i + 1]][x + dirs[i]] in valid:
                q.put((points + 1 + GetTurns(dir, i), (y + dirs[i + 1], x + dirs[i], i)))
        if iters % 10000 == 0:
            print(y, x, dir, points)
    print(best_points)
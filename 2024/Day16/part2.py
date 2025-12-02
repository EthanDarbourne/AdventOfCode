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
    NOT_VISITED = 1e9
    best_vals = np.full([n,m,4], NOT_VISITED, dtype=int)
    
    q = PriorityQueue()
    for i in range(4):
        if grid[startY + dirs[i + 1]][startX + dirs[i]] == '.':
            q.put((0, (startY, startX, i)))
    iters = 0

    valid = ['.', 'E']
    best_points = NOT_FOUND
    while not q.empty():
        points, data = q.get()
        if points > best_points:
            break
        y, x, dir = data
        if vis[y][x][dir] == 1:
            continue
        vis[y][x][dir] = 1
        best_vals[y][x][dir] = points if best_vals[y][x][dir] == NOT_VISITED else best_vals[y][x][dir]
        if endY == y and endX == x:
            best_points = points
            continue
            # break
        iters += 1
        def CheckAndAdd(y1, x1, points1, dir):
            if grid[y1][x1] in valid:
                q.put((points1, (y1, x1, dir)))

        CheckAndAdd(y + dirs[dir + 1], x + dirs[dir], points + 1, dir)
        left = (dir + 1) % 4
        right = (dir - 1) % 4
        q.put((points + 1000, (y, x, left)))
        q.put((points + 1000, (y,x, right)))

    print(best_points)


    def OppositeDir(dir):
        return (dir + 2) % 4
    # going backwards
    vis_all = np.zeros([n,m])
    def FindAllPaths(grid, best_vals, x, y, dir, vis):
        cur = best_vals[y][x][dir]
        if vis[y][x][dir] == 1 or cur == NOT_VISITED:
            return 0
        ret = 1 if vis_all[y][x] == 0 else 0
        vis_all[y][x] = 1
        vis[y][x][dir] = 1
        opposite_dir = OppositeDir(dir)
        new_y, new_x = y + dirs[opposite_dir + 1], x + dirs[opposite_dir]
        diff = cur - best_vals[new_y][new_x][dir] - 1
        if diff == 0:
            ret += FindAllPaths(grid, best_vals, new_x, new_y, dir, vis)
        up_dir = (dir + 1) % 4
        down_dir = (dir - 1) % 4
        if cur - best_vals[y][x][up_dir] == 1000:
            ret += FindAllPaths(grid, best_vals, x, y, up_dir, vis)
        if cur - best_vals[y][x][down_dir] == 1000:
            ret += FindAllPaths(grid, best_vals, x, y, down_dir, vis)

        return ret

    squares_on_best_path = 0
    vis = np.zeros([n,m,4])
    for i in range(4):
        if best_vals[endY][endX][i] == best_points:
            squares_on_best_path += FindAllPaths(grid, best_vals, endX, endY, i, vis)
    print("Answer", squares_on_best_path)
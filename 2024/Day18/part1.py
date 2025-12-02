import numpy as np
from queue import Queue

with open("input.txt", "r") as file:
    memory_landing = file.readlines()[:1024]
    n,m = 71,71
    grid = np.zeros([n,m])
    for line in memory_landing:
        x,y = [int(i.strip()) for i in line.split(',')]
        grid[x][y] = 1

    x,y,targetX,targetY = 0,0,70,70

    NOT_FOUND = 1e90 + 7
    dirs = [1, 0, -1, 0, 1] # east, north, west, south

    steps = 0
    q = Queue()
    q.put((x,y))
    while not q.empty():
        length = q.qsize()
        for i in range(length):
            x,y = q.get()
            if x < 0 or y < 0 or x == m or y == n or grid[x][y] == 1:
                continue
            grid[x][y] = 1
            if x == targetX and y == targetY:
                q = Queue()
                break
            val = NOT_FOUND
            for i in range(4):
                q.put((x + dirs[i], y + dirs[i+1]))
        steps += 1
    print(steps - 1)
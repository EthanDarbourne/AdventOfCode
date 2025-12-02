from collections import defaultdict
import numpy as np

with open('input.txt', 'r') as file:
    grid = [list(i.strip()) for i in file]

    n, m = len(grid), len(grid[0])
    d = defaultdict(list)
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                d[grid[i][j]].append((i, j))
    

    def InBounds(x, y):
        return x >= 0 and y >= 0 and x < n and y < m
    
    res = 0
    done = np.zeros([n,m]).tolist()
    for x in d:
        pos = d[x]
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                # calculate two positions of antinodes
                node1, node2 = pos[i], pos[j]
                diffX = node1[0] - node2[0]
                diffY = node1[1] - node2[1]

                newX, newY = node2[0], node2[1]
                while InBounds(newX, newY):
                    if done[newX][newY] == 0:
                        res += 1
                    done[newX][newY] = 1
                    newX, newY = newX - diffX, newY - diffY
                newX, newY = node1[0], node1[1]
                while InBounds(newX, newY):
                    if done[newX][newY] == 0:
                        res += 1
                    done[newX][newY] = 1
                    newX, newY = newX + diffX, newY + diffY
                            
    print(res)
import numpy as np
with open("input.txt", "r") as file:
    robots = []
    for line in file:
        p, v = line.split(' ')
        posX, posY = p.split('=')[1].split(',')
        vX, vY = v.split('=')[1].split(',')
        robots.append([int(posX),int(posY),int(vX),int(vY)])
    
    n, m = 101, 103
    quadrants = [0,0,0,0]

    def PrintGrid(grid):
        for i in range(n):
            print(['.' if j == 0 else int(j) for j in grid[i]])
        print()
    for i in range(103):
        grid = np.zeros([n,m])
        for robot in robots:
            posX, posY, vX, vY = robot
            posX = (posX + vX * i) % n
            posY = (posY + vY * i) % m
            robot[0] = posX
            robot[1] = posY
            grid[posX][posY] += 1
        # print(i, list(grid))
        PrintGrid(grid)
    # print(quadrants)
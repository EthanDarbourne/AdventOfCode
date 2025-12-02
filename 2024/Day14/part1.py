with open("input.txt", "r") as file:
    robots = []
    for line in file:
        p, v = line.split(' ')
        posX, posY = p.split('=')[1].split(',')
        vX, vY = v.split('=')[1].split(',')
        robots.append([int(posX),int(posY),int(vX),int(vY)])
    
    n, m = 101, 103
    quadrants = [0,0,0,0]

    for robot in robots:
        posX, posY, vX, vY = robot
        posX = (posX + vX * 100) % n
        posY = (posY + vY * 100) % m
        robot[0] = posX
        robot[1] = posY
        if posX == n // 2 or posY == m // 2:
            continue
        quadrant = posX * 2 // n + (posY * 2 // m) * 2
        quadrants[quadrant] += 1
    print(quadrants)
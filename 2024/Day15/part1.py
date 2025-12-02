
with open('input.txt', 'r') as file:

    grid = []
    while (line := file.readline()) != '\n':
        grid.append(list(line.strip()))
    
    moves = []
    while (line := file.readline()) != '':
        moves.append(list(line.strip()))
    moves = [i for j in moves for i in j]

    x, y = -1, -1
    n, m = len(grid), len(grid[0])
    for i in range(n):
        if x != -1:
            break
        for j in range(m):
            if grid[i][j] == '@':
                y, x = i, j
                break
    
    dirs = [1,0,-1,0,1]
    def MoveInDirection(x1, y1, move):
        j = 1
        while grid[y1 + j * dirs[move + 1]][x1 + j * dirs[move]] == 'O':
            j += 1
        if grid[y1 + j * dirs[move + 1]][x1 + j * dirs[move]] == '#':
            return y, x
        if j > 1:
            grid[y1 + j * dirs[move + 1]][x1 + j * dirs[move]] = 'O'
        grid[y1][x1] = '.'
        grid[y1 + dirs[move + 1]][x1 + dirs[move]] = '@'
        return y1 + dirs[move + 1], x1 + dirs[move]

    move_types = ['>', '^', '<', 'v']
    for move in moves:
        move_type = move_types.index(move)
        y, x = MoveInDirection(x, y, move_type)
        
    
    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'O':
                res += 100 * i + j
    print(res)
    
    # find robot
    # simulate movement
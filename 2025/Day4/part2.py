with open('input.txt', 'r') as file:

    grid = [list(i) for i in file.read().strip().split('\n')]

    n, m = len(grid), len(grid[0])

    dirs = [-1,-1,0,1,-1,1,1,0,-1]

    res = 0
    removed = True
    while removed:
        removed = False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '.':
                    continue
                papers = 0
                for dir in range(8):
                    r, c = i + dirs[dir], j + dirs[dir + 1]
                    if r < 0 or c < 0 or r >= n or c >= m:
                        continue
                    if grid[r][c] == '@':
                        papers += 1
                
                if papers < 4:
                    removed = True
                    grid[i][j] = '.'
                    res += 1
    print(res)

class Node:
    # offsetX is offset, offsetY is rows +/-
    def __init__(self, y, x, left = None, right = None):
        self.x = x
        self.y = y
        self.left = left
        self.right = right
        self.blocked = False

    def IsBlocked(self):
        return self.blocked or (self.left and self.left.IsBlocked()) or (self.right and self.right.IsBlocked())


with open('input.txt', 'r') as file:

    grid = []
    while (line := file.readline()) != '\n':
        grid.append(list(line.strip()))
    
    moves = []
    while (line := file.readline()) != '':
        moves.append(list(line.strip()))
    moves = [i for j in moves for i in j]

    def TransformRow(row):
        new_row = []
        for i in row:
            if i == '@' or i == '.':
                new_row.extend([i, '.'])
            elif i == 'O':
                new_row.extend(['[', ']'])
            elif i == '#':
                new_row.extend([i, i])
        return new_row
    
    grid = [TransformRow(i) for i in grid]


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
    boxes = ['[', ']']

    def MoveInDirection(x1, y1, move):

        # if horizontal, do old way
        if dirs[move] != 0:
            j = 1
            while grid[y1][x1 + j * dirs[move]] in boxes:
                j += 1
            if grid[y1][x1 + j * dirs[move]] == '#':
                return y1, x1
            for i in range(j, -1, -1):
                grid[y1][x1 + i * dirs[move]] = grid[y1][x1 + (i - 1) * dirs[move]]
            grid[y1][x1] = '.'
            grid[y1][x1 + dirs[move]] = '@'
            return y1, x1 + dirs[move]

        def GetOffsets(y, x, offset):
            if grid[y][x + offset] not in boxes:
                return []
            val = 1 if grid[y][x + offset] == '[' else -1
            return [offset, offset + val]
        
        old_offsets = []

        j = 1
        offsets = [0]

        operations = []
        while len(offsets) > 0:
            next_y = y1 + j * dirs[move + 1]
            old_y = next_y - dirs[move + 1]
            new_offsets = []
            for offset in offsets:
                cur_x = x1 + offset
                if grid[next_y][cur_x] == '#':
                    # cannot move at all
                    return y1, x1
                new_offset = GetOffsets(next_y, x1, offset)
                new_offsets.extend(new_offset)

            for offset in offsets:
                cur_x = x1 + offset
                operations.append([next_y, cur_x, grid[old_y][cur_x]])
                if offset not in old_offsets:
                    operations.append([old_y, cur_x, '.'])
            j += 1
            old_offsets = offsets
            offsets = new_offsets

        for (y2, x2, val) in operations:
            grid[y2][x2] = val

        return y1 + dirs[move + 1], x

    move_types = ['>', '^', '<', 'v']
    for move in moves:
        move_type = move_types.index(move)
        y, x = MoveInDirection(x, y, move_type)
    
    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '[':
                res += 100 * i + j
    print(res)
    
    # find robot
    # simulate movement
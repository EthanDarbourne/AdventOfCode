with open('input.txt', 'r') as file:
    
    lines = [i for i in file]

    idx = 0
    res = 0
    while idx < len(lines):
        a = lines[idx]
        b = lines[idx + 1]
        prizes = lines[idx + 2]
        idx += 4

        def Increments(l, c):
            sides = l.split(':')[1].strip().split(',')
            # print(sides, sides[1].strip().split(c))
            return [int(i.strip().split(c)[1]) for i in sides]

        one = Increments(a, '+')
        two = Increments(b, '+')
        x = [one[0], two[0]]
        y = [one[1], two[1]]

        tmp = Increments(prizes, '=')
        targetX, targetY = tmp[0], tmp[1]

        l, r = ((targetX % x[0] > 0) + targetX // x[0]), 0
        def Below(l, r):
            return l * x[0] + r * x[1] < targetX
        mins = 1e9 + 7
        while l > 0:
            val = l * x[0] + r * x[1]
            if val == targetX and l * y[0] + r * y[1] == targetY:
                mins = min(mins, 3 * l + r)
            l -= 1
            while Below(l, r):
                r += 1
        if mins != 1e9 + 7:
            res += mins
    print(res)


    
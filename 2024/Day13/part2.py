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
        targetX, targetY = tmp[0] + 0, tmp[1] + 0
        A = (targetX * y[1] - targetY * x[1]) / (x[0] * y[1] - x[1] * y[0])
        B = (targetY - A * y[0]) / y[1]
        if A % 1 == 0 and B % 1 == 0:
            res += 3 * A + B

    print(res)


    
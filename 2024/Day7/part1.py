
def CanCompute(target, l, ops, i):

    if i >= len(ops) - 1:
        return target == l
    # vals = i, i + 1
    if i == 0:
        l = ops[0]
    r = ops[i + 1]
    return CanCompute(target, l + r, ops, i + 1) or CanCompute(target, l * r, ops, i + 1)

with open('input.txt', 'r') as file:
    res = 0

    for line in file:
        sides = line.split(':')
        target = int(sides[0])
        ops = [int(i) for i in sides[1].strip().split(' ')]
        print(target, ops)
        res += target if CanCompute(target, None, ops, 0) else 0
        print(CanCompute(target, None, ops, 0))
    print(res)
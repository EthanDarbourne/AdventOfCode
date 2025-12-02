from collections import defaultdict


with open('input.txt', 'r') as file:
    before = defaultdict(list)
    lines = []
    after = False
    for line in file:
        if line == '\n':
            after = True
        elif not after:
            x,y = [int(i) for i in line.split('|')]
            before[x].append(y)
        else:
            lines.append([int(i) for i in line.split(',')])
    res = 0
    for line in lines:
        can = True
        for i in range(len(line)):
            if any(x in before[line[i]] for x in line[0:i]):
                can = False
                break
        for i in range(len(line)):
            for j in range(i):
                while line[j] in before[line[i]]:
                    line[i], line[j] = line[j], line[i]
        if not can:
            res += line[len(line) // 2]
            print(line)
    print(res)
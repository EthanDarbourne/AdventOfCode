with open('input.txt', 'r') as file:

    lines = file.read().split('\n')

    n = len(lines[0].split())
    equations = [[] for _ in range(n)]

    operations = lines.pop().split()

    for line in lines:
        nums = line.split() 
        for i in range(n):
            equations[i].append(int(nums[i]))
    
    total = 0

    for i in range(n):
        if operations[i] == '+':
            total += sum(equations[i])
        else:
            prod = 1
            for j in equations[i]:
                prod *= j
            total += prod
    print(total)
with open('input.txt', 'r') as file:
    safe_count = 0
    for line in file:
        levels = [int(i) for i in line.strip().split(' ') if i != '']


        possible = False
        for j in range(len(levels)):
            levelcopy = levels[:]
            levelcopy.pop(j)

            increasing, decreasing, remove = True, True, False
            for i in range(len(levelcopy) - 1):
                diff = levelcopy[i + 1] - levelcopy[i]
                if abs(diff) < 1 or abs(diff) > 3:
                    decreasing = increasing = False
                if diff < 0:
                    increasing = False
                elif diff > 0:
                    decreasing = False
            possible = possible or increasing or decreasing
        safe_count += 1 if possible else 0
    
    print(safe_count)

with open('input.txt', 'r') as file:
    safe_count = 0
    for line in file:
        levels = [int(i) for i in line.strip().split(' ') if i != '']

        
        increasing, decreasing = True, True
        for i in range(len(levels) - 1):
            diff = levels[i + 1] - levels[i]
            if abs(diff) < 1 or abs(diff) > 3:
                decreasing = increasing = False
            if diff < 0:
                increasing = False
            elif diff > 0:
                decreasing = False
        safe_count += 1 if increasing or decreasing else 0
    
    print(safe_count)


with open('input.txt', 'r') as file:

    ranges = []

    hitBlankLine = False
    for line in file.readlines():
        trimmed = line.strip()
        if trimmed == "":
            break
            
        parts = trimmed.split('-')
        ranges.append((int(parts[0]), int(parts[1])))
    
    sortedIntervals = []

    for r in ranges:

        start, end = r[0], r[1]
        l, r = 0, len(sortedIntervals) - 1
        while l <= r:
            mid = (l + r) // 2
            if sortedIntervals[mid][0] < start:
                l = mid + 1
            elif sortedIntervals[mid][0] == start:
                l = mid
                r = mid - 1
            else:
                r = mid - 1
        
        if l > 0 and sortedIntervals[l - 1][1] + 1 >= start:
            # merge into interval to the left
            l -= 1
        else:
            sortedIntervals.insert(l, [start, end])

        # merge overlapping intervals to the right
        while l + 1 < len(sortedIntervals) and end >= sortedIntervals[l + 1][0] - 1:
            # merge this interval
            end = max(end, sortedIntervals[l + 1][1])
            sortedIntervals.pop(l + 1)

        sortedIntervals[l][1] = max(sortedIntervals[l][1], end)

    count = 0
    for interval in sortedIntervals:
        count += interval[1] - interval[0] + 1
    print(count)

with open('input.txt', 'r') as file:

    ranges = []
    idsToCheck = []

    hitBlankLine = False
    for line in file.readlines():

        trimmed = line.strip()
        if trimmed == "":
            hitBlankLine = True
            continue
            
        if hitBlankLine:
            idsToCheck.append(int(trimmed))
        else:
            parts = trimmed.split('-')
            ranges.append((int(parts[0]), int(parts[1])))
    
    count = 0
    for id in idsToCheck:
        for r in ranges:
            if r[0] <= id <= r[1]:
                count += 1
                break
    print(count)

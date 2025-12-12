with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
    readingRegions = False
    boxes = []
    lineIdx = 0

    for i in range(6):
        lineIdx += 1 # skip first line
        allBoxes = []
        box = []
        for j in range(3):
            box.append([1 if space == "#" else 0 for space in lines[lineIdx + j]])
        boxes.append(box)
        lineIdx += 4
    
    regions = []
    for i in range(lineIdx, len(lines)):

        parts = lines[i].split(':')
        regionX, regionY = map(int, parts[0].split('x'))

        boxCounts = list(map(int, parts[1].strip().split()))
        regions.append((regionX, regionY, boxCounts))

    boxCounts = [sum(sum(x) for x in box) for box in boxes]
    enoughSpace = 0

    for region in regions:
        counts = region[2]
        total = region[0] * region[1]
        for i, j in zip(boxCounts, counts):
            total -= i * j
        if total >= 0:
            enoughSpace += 1
    print(enoughSpace)


        

    
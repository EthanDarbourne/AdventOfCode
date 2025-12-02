with open('input.txt', 'r') as file:
    line = list(file.readline())


    # expand line

    filesystem = []
    gaps = [] # index, length
    curId = 0
    space = False
    for i in range(len(line)):
        cur = int(line[i])
        if space:
            gaps.append([len(filesystem), cur])
        for j in range(cur):
            filesystem.append('.' if space else curId)
        space = not space
        curId += i % 2
    l, r = 0, len(filesystem) - 1

    while r >= 0:
        # find next non-dot
        # swap
        while filesystem[r] == '.':
            r -= 1
        # find length of this segment
        curId = filesystem[r]
        l = r
        while filesystem[l] == curId:
            l -= 1
        length = r - l
        for gap in gaps:
            if gap[1] >= length and gap[0] < r:
                # place here
                for i in range(length):
                    filesystem[r - i] = '.'
                    filesystem[i + gap[0]] = curId
                gap[1] -= length
                gap[0] += length
                break
        r = l
    checksum = 0
    for i in range(len(filesystem)):
        if filesystem[i] == '.':
            continue
        checksum += i * filesystem[i]
    # print(filesystem)
    print(checksum)
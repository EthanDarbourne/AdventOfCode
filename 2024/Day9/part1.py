with open('input.txt', 'r') as file:
    line = list(file.readline())


    # expand line

    filesystem = []
    curId = 0
    space = False
    for i in range(len(line)):
        cur = int(line[i])
        for j in range(cur):
            filesystem.append('.' if space else curId)

        space = not space
        curId += i % 2
    l, r = 0, len(filesystem) - 1

    while l < r:
        # find next dot
        # find next non-dot
        # swap
        while filesystem[l] != '.':
            l += 1
        while filesystem[r] == '.':
            r -= 1
        filesystem[l], filesystem[r] = filesystem[r], filesystem[l]
        l += 1
        r -= 1
    checksum = 0
    for i in range(len(filesystem)):
        if filesystem[i] == '.':
            break
        checksum += i * filesystem[i]
    # print(filesystem)
    print(checksum)
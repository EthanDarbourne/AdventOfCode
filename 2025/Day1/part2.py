

with open('input.txt', 'r') as file:
    start = 50

    totalLength = 100
    zeroCount = 0

    for line in file:
        direction, distance = line[0], int(line[1:])
        if direction == 'L':
            if start == 0:
                zeroCount -= 1
            start = start - distance
            zeroCount += (totalLength - start) // totalLength
        elif direction == 'R':
            start = (start + distance)
            zeroCount += start // totalLength
        start %= totalLength
    print(zeroCount)
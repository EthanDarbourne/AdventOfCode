

with open('input.txt', 'r') as file:
    start = 50

    totalLength = 100
    zeroCount = 0

    for line in file:
        direction, distance = line[0], int(line[1:])
        if direction == 'L':
            start = (start - distance + totalLength) % totalLength
        elif direction == 'R':
            start = (start + distance) % totalLength
        if start == 0:
            zeroCount += 1
    print(zeroCount)
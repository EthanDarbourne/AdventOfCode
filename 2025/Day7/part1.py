with open('input.txt', 'r') as file:

    lines = file.read().split('\n')

    beamLocations = [lines[0].index("S")]
    n, m = len(lines), len(lines[0])

    splits = 0
    for i in range(1, n):
        newBeamLocations = set()
        for j in beamLocations:
            if lines[i][j] == '^':
                splits += 1
                newBeamLocations.add(j-1)
                newBeamLocations.add(j+1)
            else:
                newBeamLocations.add(j)
        beamLocations = newBeamLocations
    print(splits)
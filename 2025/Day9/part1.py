with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

    corners = [tuple([int(x) for x in i.split(',')]) for i in lines]

    def CalculateArea(c1, c2):

        deltaY = abs(c1[1] - c2[1]) + 1
        deltaX = abs(c1[0] - c2[0]) + 1
        return deltaX * deltaY

    bestRect = 0
    n = len(corners)
    for i in range(n):
        for j in range(i + 1, n):
            bestRect = max(bestRect, CalculateArea(corners[i], corners[j]))
    print(bestRect)

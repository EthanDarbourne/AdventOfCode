from shapely.geometry.polygon import Polygon
from shapely import box

with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

    corners = [tuple([int(x) for x in i.split(',')]) for i in lines]
    n = len(corners)

    polygon = Polygon(corners)
    def CalculateArea(c1, c2):
        deltaY = abs(c1[1] - c2[1]) + 1
        deltaX = abs(c1[0] - c2[0]) + 1
        return deltaX * deltaY
    
    bestRect = 0
    for i in range(n):
        for j in range(i + 1, n):
            left, right = min(corners[i][0], corners[j][0]), max(corners[i][0], corners[j][0])
            top, bottom = min(corners[i][1], corners[j][1]), max(corners[i][1], corners[j][1])
            inner = box(left, top, right, bottom)

            area = CalculateArea(corners[i], corners[j])
            if area < bestRect:
                continue
            if polygon.contains(inner):
                bestRect = area
    print(bestRect)
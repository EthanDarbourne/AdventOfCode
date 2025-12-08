import heapq
import math

with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

    closestPairs = []
    junctionBoxes = [tuple([int(x) for x in i.split(',')]) for i in lines]
    n = len(junctionBoxes)

    def ComputeDistanceTuple(box1, box2):
        dist = 0
        for i in range(len(box1)):
            dist += pow(box1[i] - box2[i], 2)
        return (-math.sqrt(dist), box1, box2)

    for i in range(n):
        for j in range(i + 1, n):
            heapq.heappush(closestPairs, ComputeDistanceTuple(junctionBoxes[i], junctionBoxes[j]))
            if len(closestPairs) > 1000:
                heapq.heappop(closestPairs)

    circuits = []
    heapq._heapify_max(closestPairs)
    while len(closestPairs) > 0:
        (distance, box1, box2) = heapq.heappop(closestPairs)
        box1Index = -1
        box2Index = -1
        for i in range(len(circuits)):
            if box1 in circuits[i]:
                box1Index = i
            if box2 in circuits[i]:
                box2Index = i
        
        if box1Index == -1 and box2Index == -1:
            circuits.append([box1,box2])
        elif box1Index == box2Index:
            continue
        elif box1Index == -1:
            circuits[box2Index].append(box1)
        elif box2Index == -1:
            circuits[box1Index].append(box2)
        else:
            circuits[box1Index].extend(circuits[box2Index])
            circuits.pop(box2Index)
    
    longestCircuits = sorted([len(circuit) for circuit in circuits])[-3:]
    print(longestCircuits)
    print(longestCircuits[0] * longestCircuits[1] * longestCircuits[2])

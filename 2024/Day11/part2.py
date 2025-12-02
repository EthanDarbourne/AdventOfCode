from collections import defaultdict
from queue import Queue
def CountDigits(k):
    old = k
    cnt = 1
    while (k := k // 10) > 0:
        cnt += 1
        
    if cnt % 2:
        return False
    half = 10 ** (cnt // 2)
    return (old // half, old % half)

class Node:
    def __init__(self, created, data = None):
        self.created = created
        self.data = data
        self.children = []
        self.ignore = False

    def GetCount(self):
        if self.ignore:
            return 0
        count = 1
        for child in self.children:
            count += child.GetCount()
        return count
    
    def AddChild(self, child):
        self.children.append(child)

with open('input.txt', 'r') as file:
    line = list(int(i) for i in file.readline().split(' '))


    processed = defaultdict(lambda: [-1] * 76)
    def Calculate(root, blinks): # blinks completed
        cnt = 1
        for child in root.children:
            # print(child)
            cnt += Calculate(child, blinks)
        processed[root.data][blinks - root.created] = cnt
        return cnt
        

    def Process(k):
        res = 0
        root = Node(0, k)
        q = Queue()
        q.put(root)
        blinks = 25
        for i in range(blinks):
            print(i + 1, q.qsize())
            n = q.qsize()
            for _ in range(n):
                front = q.get()
                if processed[front.data][blinks - i - 1] != -1:
                    assert(len(front.children) == 0)
                    print("OMG PREPROCESS")
                    res += processed[front.data][blinks - i - 1]
                    front.ignore = True
                    continue
                if front.data == 0:
                    front.data = 1
                elif (sides := CountDigits(front.data)):
                    front.data = sides[0]
                    front.AddChild(Node(i + 1, sides[1]))
                else:
                    front.data *= 2024

                Calculate(root, i + 1)
                
                q.put(front)
                for node in front.children:
                    q.put(node)
        return res
    

    res = 0
    q = Queue()
    for i in line:
        res += Process(i)
        print("Process")
    print(processed)
#     def Process(k, blinks):
#         old = k
#         res = 1
#         if processed[k][blinks] != -1:
#             return processed[k][blinks]
#         cur = [k]
#         for j in range(blinks):
#             n = len(cur)
#             for k in range(n):
#                 if cur[k] == 0:
#                     cur[k] = 1
#                 elif (sides := CountDigits(cur[k])):
#                     cur[k] = sides[0]
#                     cur.append(sides[1])
#                 else:
#                     cur[k] *= 2024
#             processed[old][j + 1] = len(cur)
#         return res
    print(res)
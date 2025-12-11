from collections import defaultdict

with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

    edges = {}
    for line in lines:
        parts = line.split(":")
        edges[parts[0]] = parts[1].strip().split()
    
    memo = {}

    def dfs(cur, curPath, target):
        if cur == target:
            if "dac" in curPath and "fft" in curPath:
                return 1
            return 0
        if cur in curPath:
            return 0
        
        memoKey = (cur, "dac" in curPath, "fft" in curPath)
        if memoKey in memo:
            return memo[memoKey]
        
        paths = 0
        curPath.append(cur)
        for edge in edges[cur]:
            paths += dfs(edge, curPath[:], target)
        memo[memoKey] = paths
        return paths

    total_paths = dfs("svr", [], "out")
    print(total_paths)
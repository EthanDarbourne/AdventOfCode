with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

    edges = {}

    for line in lines:
        parts = line.split(":")
        edges[parts[0]] = parts[1].strip().split()
    
    memo = {}
    def dfs(cur, curPath):
        if cur == "out":
            return 1
        if cur in curPath:
            return 0
        if cur in memo:
            return memo[cur]
        paths = 0
        curPath.append(cur)
        for edge in edges[cur]:
            paths += dfs(edge, curPath[:])
        memo[cur] = paths
        return paths

    total_paths = dfs("you", [])
    print(total_paths)
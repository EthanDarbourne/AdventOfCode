from collections import defaultdict

with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

    edges = {}
    edges["out"] = []
    for line in lines:
        parts = line.split(":")
        edges[parts[0]] = parts[1].strip().split()
    
    memo = defaultdict(dict)

    def GetFromMemo(memo, cur, isDac, isFft):
        if cur in memo:
            if isDac:
                if isFft:
                    if "dac-fft" in memo[cur]:
                        return memo[cur]["dac-fft"]
                else:
                    if "dac" in memo[cur]:
                        return memo[cur]["dac"]
            elif isFft:
                if "fft" in memo[cur]:
                    return memo[cur]["fft"]
            else:
                if 0 in memo[cur]:
                    return memo[cur][0]
        return -1        
        
    def PutInMemo(memo, cur, isDac, isFft, paths):
        if isDac:
            if isFft:
                memo[cur]["dac-fft"] = paths
            else:
                memo[cur]["dac"] = paths
        elif isFft:
            memo[cur]["fft"] = paths
        else:
            memo[cur][0] = paths


    def dfs(cur, curPath, target):
        if cur == target:
            if "dac" in curPath and "fft" in curPath:
                return 1
            return 0
        if cur in curPath:
            return 0
        fromMemo = GetFromMemo(memo, cur, "dac" in curPath, "fft" in curPath)
        if fromMemo != -1:
            return fromMemo
        
        paths = 0
        curPath.append(cur)
        for edge in edges[cur]:
            paths += dfs(edge, curPath[:], target)
        PutInMemo(memo, cur, "dac" in curPath, "fft" in curPath, paths)
        return paths

    total_paths = dfs("svr", [], "out")
    print(total_paths)
with open('input.txt', 'r') as file:

    lines = file.read().split('\n')
    n, m = len(lines), len(lines[0])

    memo = {}
    def dfs(lineNum, index):
        key = (lineNum, index)
        if key in memo:
            return memo[key] 
        if lineNum >= n:
            return 1
        result = 0
        if lines[lineNum][index] == '^':
            result = dfs(lineNum, index + 1) + dfs(lineNum, index - 1)
        else:
            result = dfs(lineNum + 1, index)
        memo[key] = result
        return result

    beamLocation = lines[0].index("S")

    print(dfs(0, beamLocation))
            
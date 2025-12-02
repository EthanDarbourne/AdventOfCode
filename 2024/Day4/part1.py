with open('input.txt', 'r') as file:

    matrix = [list(line[:-1] if line[-1] == '\n' else line) for line in file]
    
    n, m = len(matrix), len(matrix[0])
    result = 0

    def Check(s):
        return 1 if s == "XMAS" or s == "SAMX" else 0
    for i in range(n):
        for j in range(m):
            s, t = '', ''
            if i <= n - 4:
                s = ''.join(x[j] for x in matrix[i:i + 4])
            if j <= m - 4:
                t = ''.join(matrix[i][j: j + 4])
            # print(s, t)
            result += Check(s) + Check(t)
            if i <= n - 4 and j <= m - 4:
                u,v = '', ''
                for k in range(4):
                    u += matrix[i + k][j + k]
                    v += matrix[i + 3 - k][j + k]
                print(u,v)
                result += Check(u) + Check(v)
    print(result)
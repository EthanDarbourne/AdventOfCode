with open('input.txt', 'r') as file:

    matrix = [list(line[:-1] if line[-1] == '\n' else line) for line in file]
    
    n, m = len(matrix), len(matrix[0])
    result = 0

    def Check(s):
        if s[1][1] != 'A':
            return 0
        valid = ['S', 'M']
        if (s[0][0] in valid and s[2][2] in valid and s[2][2] != s[0][0]) and (s[0][2] in valid and s[2][0] in valid and s[2][0] != s[0][2]):
            return 1
        return 0
    for i in range(n - 2):
        for j in range(m - 2):

            s = [''.join(x[j:j + 3]) for x in matrix[i: i + 3]]
            result += Check(s)
    print(result)
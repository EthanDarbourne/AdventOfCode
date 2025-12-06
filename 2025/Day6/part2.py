with open('input.txt', 'r') as file:

    lines = file.read().split('\n')

    n = len(lines[0].split())
    equations = [[] for _ in range(n)]

    operations = lines.pop().split()

    total = 0

    def EvaluateEquation(vals, operation):
        print(vals)
        vals = [int(val) for val in vals if val != '']
        if operation == '+':
            return sum(vals)
        elif operation == '*':
            prod = 1
            for val in vals:
                prod *= val
            return prod
        else:
            raise Exception("Invalid operation")


    vals = ["", "", "", ""]
    operationIdx = 0
    idx = 0
    for i in range(len(lines[0])):
        isSpaces = True
        for j in range(len(lines)):
            if lines[j][i] != ' ':
                isSpaces = False
                vals[idx] += lines[j][i]
        idx += 1
        if isSpaces:
            total += EvaluateEquation(vals, operations[operationIdx])
            operationIdx += 1
            idx = 0
            vals = ["", "", "", ""]
    total += EvaluateEquation(vals, operations[operationIdx])
    print(total)
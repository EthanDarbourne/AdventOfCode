with open('input.txt', 'r') as file:
    result = 0
    s = ''.join(file)
    for i in range(len(s)):
        mulcheck = s[i:i + 3]
        if mulcheck != "mul" or s[i + 3] != '(':
            continue

        next = s[i + 4: i + 12]
        print(next)
        index = 0
        x,y = '', ''
        for j in range(3):
            if next[index].isdigit():
                x += next[index]
            else:
                break
            index += 1
        if next[index] != ',':
            continue
        index += 1
        for j in range(3):
            if next[index].isdigit():
                y += next[index]
            else:
                break
            index += 1
        if next[index] != ')':
            continue
        result += int(x) * int(y)
    print(result)
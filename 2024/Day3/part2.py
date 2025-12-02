with open('input.txt', 'r') as file:
    result = 0
    s = ''.join(file)
    do = True
    for i in range(len(s)):
        docheck = s[i: i + 4]
        if docheck == "do()":
            do = True
        dontcheck = s[i:i+ 7]
        if dontcheck == "don't()":
            do = False

        mulcheck = s[i:i + 3]
        if do == False or mulcheck != "mul" or s[i + 3] != '(':
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
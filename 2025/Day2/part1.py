
with open('input.txt', 'r') as file:
    
    line = file.readline()
    ranges = [(int(x.split('-')[0]), int(x.split('-')[1])) for x in (line.strip().split(','))]

    res = 0
    for r in ranges:
        
        for i in range(r[0], r[1] + 1):
            if len(str(i)) % 2 == 1:
                continue
            mid = len(str(i)) // 2
            if str(i)[:mid] == str(i)[mid:]:
                res += i
    print(res)

with open('input.txt', 'r') as file:
    
    line = file.readline()
    ranges = [(int(x.split('-')[0]), int(x.split('-')[1])) for x in (line.strip().split(','))]

    res = 0
    for r in ranges:
        
        for i in range(r[0], r[1] + 1):
            
            num = str(i)
            length = len(num)
            for splitLength in range(1, 1 + length // 2):
                if length % splitLength != 0:
                    continue
                found = True
                idx = 0
                for k in range(length):
                    if num[k] != num[idx]:
                        found = False
                        break
                    idx = (idx + 1) % splitLength
                if found:
                    res += i
                    break
    print(res)
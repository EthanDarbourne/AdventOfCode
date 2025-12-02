
def CountDigits(k):
    old = k
    cnt = 1
    while (k := k // 10) > 0:
        cnt += 1
        
    if cnt % 2:
        return False
    half = 10 ** (cnt // 2)
    return (old // half, old % half)


with open('input.txt', 'r') as file:
    line = list(int(i) for i in file.readline().split(' '))

    res = 0
    for i in line:
        cur = [i]
        for _ in range(25):
            n = len(cur)
            for k in range(n):
                if cur[k] == 0:
                    cur[k] = 1
                elif (sides := CountDigits(cur[k])):
                    cur[k] = sides[0]
                    cur.append(sides[1])
                else:
                    cur[k] *= 2024
        res += len(cur)
    print(res)
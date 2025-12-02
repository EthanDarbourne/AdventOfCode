with open('input.txt', 'r') as file:
    left, right = [], []
    for line in file:
        # print(line)
        nums = [int(i) for i in line.strip().split(' ') if i != '']
        left.append(nums[0])
        right.append(nums[1])
    res = 0
    for i in left:
        res += i * right.count(i)
    print(res)
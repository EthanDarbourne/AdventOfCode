

with open('input.txt', 'r') as file:
    left, right = [], []
    for line in file:
        # print(line)
        nums = [int(i) for i in line.strip().split(' ') if i != '']
        left.append(nums[0])
        right.append(nums[1])
    
    left.sort()
    right.sort()
    
    res = 0
    for i in range(len(left)):
        res += abs(left[i] - right[i])
        print(left[i], right[i], abs(left[i] - right[i]))
    print(res)
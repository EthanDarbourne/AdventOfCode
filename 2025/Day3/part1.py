with open('input.txt', 'r') as file:
    voltage = 0
    for line in file.readlines():
        first, second = -1, -1

        nums = [int(i) for i in line[:-1]]
        for i in range(len(nums) - 1):
            if nums[i] > first:
                first = nums[i]
                second = nums[i+1]
            if nums[i+1] > second:
                second = nums[i+1]
        voltage += 10 * first + second
    print(voltage)
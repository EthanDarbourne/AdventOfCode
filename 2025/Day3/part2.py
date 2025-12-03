
def GetDropIndex(nums):
    index = 11
    for i in range(10, -1, -1):
        if nums[i] < nums[i+1]:
            index = i
    return index

with open('input.txt', 'r') as file:
    voltage = 0
    for line in file.readlines():
        nums = [int(i) for i in line.strip()]
        n = len(nums)
        
        batteries = nums[-12:]
        minBattery = min(batteries)

        for i in range(n - 13, -1, -1):
            # if incoming number would make current number larger, take that number and remove number that is holding us back
            # or the earliest number that is smaller than the one after it
            if nums[i] >= batteries[0]:
                batteries.pop(GetDropIndex(batteries))
                batteries.insert(0, nums[i])
                minBattery = min(batteries)
        for i in range(12):
            voltage += batteries[-1 - i] * pow(10, i)
    print(voltage)

with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

    class Machine:

        def __init__(self, lights, buttons, joltages):
            self.lights = [1 if light == '#' else 0 for light in lights[1:-1]]
            self.buttons = [list(map(int,button[1:-1].split(','))) for button in buttons]
            self.joltages = list(map(int, joltages[1:-1].split(',')))

        def __str__(self):
            return f"Lights: {self.lights}\nButtons: {self.buttons}\nJoltages: {self.joltages}"
    
    def Flip(num):
        return 1 if num == 0 else 0
    
    def FlipButtons(start, buttons):
        res = start.copy()
        for button in buttons:
            res[button] = Flip(res[button])
        return res
    
    def CalculateButtonPresses(machine: Machine):
        
        target = machine.lights
        n = len(target)
        buttonCnt = len(machine.buttons)
       
        q = [([0] * n, 0)] # state = (curLights, curIndex)
        buttonsPressed = -1
        while len(q) > 0:
            cnt = len(q)
            buttonsPressed += 1

            for _ in range(cnt):
                curLights, curIndex  = q.pop(0)
                if curLights == target:
                    q = []
                    break
                
                for j in range(curIndex, buttonCnt):
                    q.append((FlipButtons(curLights, machine.buttons[j]), j + 1))

        return buttonsPressed
    
    totalButtons = 0
    for line in lines:
        parts = line.split()

        machine = Machine(parts[0], parts[1:-1], parts[-1])
        totalButtons += CalculateButtonPresses(machine)
    
    print(totalButtons)
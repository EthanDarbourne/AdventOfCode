
from scipy.optimize import linprog

with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

    class Machine:

        def __init__(self, lights, buttons, joltages):
            self.lights = [1 if light == '#' else 0 for light in lights[1:-1]]
            self.buttons = [list(map(int,button[1:-1].split(','))) for button in buttons]
            self.joltages = list(map(int, joltages[1:-1].split(',')))

        def __str__(self):
            return f"Lights: {self.lights}\nButtons: {self.buttons}\nJoltages: {self.joltages}"

    def CreateLinearProgramAndSolve(machine: Machine):
        
        buttonCnt = len(machine.buttons)
        joltageCnt = len(machine.joltages)

        # objective function: minimize number of button presses
        objective = [1] * buttonCnt

        # make sure every button press count is >= 0, (-x_1 <= 0)
        A_ub = []
        for i in range(buttonCnt):
            A_ub.append([0] * buttonCnt)
            A_ub[-1][i] = -1
        b_ub = [0] * buttonCnt

        # each button press affects certain voltages. Sum of buttons = voltages
        A_eq = []
        b_eq = machine.joltages

        for i in range(joltageCnt):
            buttonsPressing = []
            for j in range(buttonCnt):
                buttonsPressing.append(1 if i in machine.buttons[j] else 0)
            A_eq.append(buttonsPressing)
        return linprog(c=objective, A_ub=A_ub, b_ub=b_ub,A_eq=A_eq, b_eq=b_eq, integrality=objective)
        
    totalButtons = 0
    for line in lines:
        parts = line.split()

        machine = Machine(parts[0], parts[1:-1], parts[-1])
        totalButtons += CreateLinearProgramAndSolve(machine).fun
    
    print(int(totalButtons))

def GetRegister(line):
    return int(line.split(':')[1].strip())
A,B,C = None,None,None
def GetComboOperand(val):
    super = [A,B,C]
    return val if val < 4 else super[val - 4]
with open("input.txt", "r") as file:
    lines = file.readlines()
    A, B, C = [GetRegister(val) for val in lines[0:3]]
    program = [int(i) for i in lines[-1].split(':')[1].strip().split(',')]
    output = []
    n = len(program)
    instruction_pointer = 0
    while instruction_pointer + 1 < n:
        opcode, operand = program[instruction_pointer:instruction_pointer+2]
        combo_operand = GetComboOperand(operand)
        if opcode == 0:
            A //= pow(2,combo_operand)
        elif opcode == 1:
            B = B ^ operand
        elif opcode == 2:
            B = combo_operand % 8
        elif opcode == 3:
            if A != 0:
                instruction_pointer = operand
                continue
        elif opcode == 4:
            B = B ^ C
        elif opcode == 5:
            output.append(combo_operand % 8)
        elif opcode == 6:
            B = A // pow(2, combo_operand)
        elif opcode == 7:
            C = A // pow(2, combo_operand)
        instruction_pointer += 2
    print(','.join(map(str,output)))
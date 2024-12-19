import re 

def evaluate(program, registers, ip=0):
    out = []
    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]
        
        if opcode == 0:
            registers[0] //= (2 ** combo_operand(operand, registers))
        elif opcode == 1:
            registers[1] ^= operand
        elif opcode == 2:
            registers[1] = combo_operand(operand, registers) % 8
        elif opcode == 3:
            # Jump to next spot in program, do not increment.
            if registers[0] != 0:
                ip = operand
                continue
        elif opcode == 4:
            registers[1] ^= registers[2]
        elif opcode == 5:
            out.append(combo_operand(operand, registers) % 8)
        elif opcode == 6:
            registers[1] = registers[0] // (2 ** combo_operand(operand, registers))
        elif opcode == 7:
            registers[2] = registers[0] // (2 ** combo_operand(operand, registers))
        else:
            raise ValueError("Unrecognized opcode.")
        
        # Increment the pointer
        ip += 2
        
    # Return result of the program 
    return ",".join(map(str, out))

def combo_operand(operand, registers):
    if operand == 4:
        return registers[0]
    elif operand == 5:
        return registers[1]
    elif operand == 6:
        return registers[2]
    else:
        return operand

with open('input.txt') as file:
    content = file.read()
    
content = content.split("\n\n")
registers = list(map(int, re.findall(r"-?\d+", content[0])))
program = list(map(int, re.findall(r"-?\d+", content[1])))

result = evaluate(program, registers)
print(result)
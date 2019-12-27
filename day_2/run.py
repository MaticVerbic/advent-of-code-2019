import traceback
from itertools import product

# Define constants. 
OP_END = 99
OP_ADD = 1
OP_MUL = 2

ERR_OPCODE = "invalid operand code %d"

# Reads data from the provided input file. 
def getData():
    with open("/files/day_2/input.txt") as file:
        for  line in file: 
            # Split and convert to int
            return [int(i) for i in line.split(",")]
    return []

# Defines a possible mathematical operation and returns a result. 
def operation(opCode, operandOne, operandTwo):     
    if opCode == OP_ADD:
        return operandOne + operandTwo

    if opCode == OP_MUL:
        return operandOne * operandTwo 
    
    raise Exception(ERR_OPCODE % opCode)
        

# Parses and returns an instruction set.
def parse(data, noun, verb):
    commands = data.copy()
    commands[1] = noun
    commands[2] = verb

    for i in range(0, len(commands), 4):
        # Get opcode. 
        opCode = commands[i]

        # Check for exit condition. 
        if opCode == OP_END: 
            return commands
            
        resultIndex = commands[i+3]

        # Get values. 
        operandOne, operandTwo = commands[commands[i+1]], commands[commands[i+2]]


        # Perform the operation
        commands[resultIndex] = operation(opCode, operandOne, operandTwo)

    return commands


if __name__ == "__main__":
    try:
        data = getData() 
        print("(task1): Result in index one: ", parse(data, 12, 2)[0])
        data = getData()
        for noun, verb in product(range(0, 100), range(0, 100)):
            if parse(data, noun, verb)[0] == 19690720:
                print("(task2): Noun: %d, Verb: %d, Result: %d" % (noun, verb, 100 * noun + verb))
                break
    except Exception as e:
        traceback.print_exc()
 
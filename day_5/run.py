'''
@author: Matic Verbic

Solution for https://adventofcode.com/2019/day/5
'''

import traceback
import logging
from itertools import product

# Define constants. 
OP_END = 99
OP_ADD = 1
OP_MUL = 2
OP_W = 3
OP_R = 4

ERR_OPCODE = "failed to parse operand code: \"{}\""
ERR_INPUT = "failed to parse input: \"{}\""
ERR_OUTPUT = "failed to print output"
ERR_MODES = "invalid mode value at index \"{}\""

SET_OUTPUT_LEVEL="failed"

# Reads data from the provided input file. 
def getData():
    with open("day_5/input.txt") as file:
        for  line in file: 
            # Split and convert to int
            return [int(i) for i in line.split(",")]
    return []

# Defines a possible mathematical operation and returns a result. 
def handler_math(opCode, operandOne, operandTwo):     
    if opCode == OP_ADD:
        return operandOne + operandTwo

    if opCode == OP_MUL:
        return operandOne * operandTwo 
    
# Handles input/output operations. 
def handler_io(opCode, position, data):
    # Handle writes. 
    if opCode == OP_W:
        try: 
            data[position] = int(input("Input (expected input here is 1): "))
        except Exception as e:
            raise Exception(ERR_INPUT.format(inp))

    # Handle reads. 
    if opCode == OP_R: 
        try: 
            if data[position] != 0: 
                print("(task1): {}".format(data[position]))
        except Exception as e:
            raise Exception(ERR_OUTPUT)
            
# Parses new format of operation codes. 
def handler_opcode(opcode):
    # Validate lambda. 
    validate = lambda x: True if x in (0, 1) else False
    
    # Reverse the number and sum.
    op = [int(x) * (10 ** i) for i, x in enumerate(str(opcode)[:-3:-1])]
    
    # Generate other commands, valid responses: 1, 0; invalid response: -1. 
    modes = [int(x) if validate(int(x)) else -1 for x in str(opcode)[-3::-1]]

    # If invalid values are found throw an exception. 
    if -1 in modes: 
        raise Exception(ERR_MODES.format(1 + modes.index(-1)))

    # Return [opcode, mode param 1, mode param 2, mode param 3]. 
    return [sum(op)] + modes + [0 for _ in range(4 - (1 + len(modes)))]
    
# Parses and returns an instruction set.
def parse(data, noun=12, verb=2, mode=0):
    commands = data.copy()
    if mode == 0: 
        commands[1] = noun
        commands[2] = verb

    i = 0
    while i < len(commands): 
        # Get opcode. 
        opCode = handler_opcode(commands[i])

        # Check for exit condition. 
        if opCode[0] == OP_END: 
            opLog(99, "END", opCode)
            return commands
        
        # Handle I/O. 
        if opCode[0] in [OP_R, OP_W]: 
            addr = commands[i+1]
            opLog(99, "READ" if opCode[0] == OP_R else "WRITE", opCode, addr)
            handler_io(opCode[0], addr, commands)

            i += 2 
            continue

        # Handle arithmetic operations. 
        if opCode[0] in [OP_ADD, OP_MUL]:
            resultIndex = commands[i+3] 

            # Get values. 
            operandOne = commands[i+1] if opCode[1] == 1 else commands[commands[i+1]]
            operandTwo = commands[i+2] if opCode[2] == 1 else commands[commands[i+2]]
            
            # Perform the mathematical operation
            opLog(0, "ADD" if opCode[0] == OP_ADD else "MUL", opCode, operandOne, operandTwo, resultIndex)
            commands[resultIndex] = handler_math(opCode[0], operandOne, operandTwo)

            i += 4
            continue 

        # Invalid opcode was provided, execution error. 
        raise Exception(ERR_OPCODE.format(opCode[0]))
        break
    return commands

# Helper method for logging. 
def init_logger(): 
    logger = logging.getLogger(__name__)
    syslog = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s: %(message)s')
    syslog.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(syslog)

    logger.disabled = True # To enable the logger comment this line. 
    return logging.LoggerAdapter(logger, {})

# Helper method for logging. 
def opLog(mode, op, opCode, operandOne=None, operandTwo=None, resultIndex=None):
    # Log IO operations. 
    if mode == 1:
        logger.info({
            "operation": op,
            "opCode": opCode,
            "operandOne": operandOne,
        })

    # Log arithmetic operations. 
    if mode == 0: 
        logger.info({
            "operation": op,
            "opCode": opCode,
            "operandOne": operandOne,
            "operandTwo": operandTwo,
            "resultIndex": resultIndex,
        })

    # Log exit. 
    if mode == 99:
        logger.info({
            "operation": op,
            "opCode": opCode,
        })


if __name__ == "__main__":
    try:
        # Init the logger. 
        logger = init_logger()
        
        # Task one. 
        data = getData() 
        parse(data, mode=1)

    except Exception as e:
        traceback.print_exc()
 
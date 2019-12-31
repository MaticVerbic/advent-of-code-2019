'''
@author: Matic Verbic

Solution for https://adventofcode.com/2019/day/5
'''

import traceback
import logging
from itertools import product

# Define constants. 
OP_END = 99 # Exit
OP_ADD = 1  # Addition
OP_MUL = 2  # Multiplication
OP_W = 3    # Write to memory
OP_R = 4    # Read from memory
OP_JMT = 5  # Jump when true
OP_JMF = 6  # Jump when false
OP_LT = 7   # Less than
OP_EQ = 8   # Equal
OP_GT = 9   # Greater than

ERR_OPCODE = "failed to parse operand code: \"{}\""
ERR_INPUT = "failed to parse input: \"{}\""
ERR_OUTPUT = "failed to print output"
ERR_MODES = "invalid mode value at index \"{}\""

# Reads data from the provided input file. 
def getData(task):
    with open("day_5/input.txt") as file:
        for  line in file: 
            # Split and convert to int
            return [int(i) for i in line.split(",")]
    return []

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

# Defines a possible mathematical operation and returns a result. 
def handler_math(opCode, operandOne, operandTwo):     
    if opCode == OP_ADD:
        return operandOne + operandTwo

    if opCode == OP_MUL:
        return operandOne * operandTwo 
    
# Handles input/output operations. 
def handler_io(opCode, position, data, task):
    # Handle writes. 
    if opCode == OP_W:
        try: 
            data[position] = int(input("Input(expected input is {}): ".format("1" if task == 1 else "5")))
            return
        except Exception as e:
            raise Exception(ERR_INPUT.format(inp))

    # Handle reads. 
    if opCode == OP_R: 
        try: 
            if task == 1 and data[position] == 0: 
                return    
            print("(task{}): {}".format(task, data[position]))
        except Exception as e:
            raise Exception(ERR_OUTPUT)

# Handles jump operations. 
def handler_jump(i, opCode, operandOne, operandTwo):
    return operandTwo if handler_compare(opCode, operandOne) else i + 3

def handler_compare(opCode, operandOne, operandTwo=None):
    # Handle if true.
    if opCode[0] == OP_JMT:
        return bool(operandOne)

    # Handle if false
    if opCode[0] == OP_JMF:
        return not bool(operandOne) 
    
    if opCode[0] == OP_GT: 
        return operandOne > operandTwo
    
    if opCode[0] == OP_LT: 
        return operandOne < operandTwo
    
    if opCode[0] == OP_EQ:
        return operandOne == operandTwo

# Parses and returns an instruction set.
def parse(data, noun=12, verb=2, mode=0, task=1):
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
            mode = "READ" if opCode[0] == OP_R else "WRITE"
            addr = commands[i+1]

            opLog(99, mode, opCode, resultIndex=addr)
            handler_io(opCode[0], addr, commands, task)

            i += 2 
            continue

        # Handle arithmetic operations. 
        if opCode[0] in [OP_ADD, OP_MUL]:
            mode = "ADD" if opCode[0] == OP_ADD else "MUL"
            resultIndex = commands[i+3] 

            # Get values. 
            operandOne = commands[i+1] if opCode[1] == 1 else commands[commands[i+1]]
            operandTwo = commands[i+2] if opCode[2] == 1 else commands[commands[i+2]]
            
            # Perform the mathematical operation
            opLog(0, mode, opCode, operandOne, operandTwo, resultIndex)
            commands[resultIndex] = handler_math(opCode[0], operandOne, operandTwo)

            i += 4
            continue 
        
        # Handle jumps. 
        if opCode[0] in [OP_JMT, OP_JMF]:
            mode = "JMT" if opCode[0] == OP_JMT else "JMF"

            # Get values. 
            operandOne = commands[i+1] if opCode[1] == 1 else commands[commands[i+1]]
            operandTwo = commands[i+2] if opCode[2] == 1 else commands[commands[i+2]]

            # Parse jump. 
            i = handler_jump(i, opCode, operandOne, operandTwo)

            opLog(2, mode, opCode, operandOne, operandTwo)
            continue
        
        # Handle boolean expressions. 
        if opCode[0] in [OP_LT, OP_EQ, OP_GT]:
            resultIndex = commands[i+3] 

            # Get values. 
            operandOne = commands[i+1] if opCode[1] == 1 else commands[commands[i+1]]
            operandTwo = commands[i+2] if opCode[2] == 1 else commands[commands[i+2]]

            # Set value
            opLog(0, mode, opCode, operandOne, operandTwo, resultIndex)
            commands[resultIndex] = 1 if handler_compare(opCode, operandOne, operandTwo) else 0
            
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
    # Log arithmetic and boolean operations. 
    if mode == 0: 
        logger.info({
            "operation": op,
            "opCode": opCode,
            "operandOne": operandOne,
            "operandTwo": operandTwo,
            "resultIndex": resultIndex,
        })

    # Log IO operations. 
    if mode == 1:
        logger.info({
            "operation": op,
            "opCode": opCode,
            "operandOne": operandOne,
        })
    
    # Log jumps. 
    if mode == 2: 
        logger.info({
            "operation": op,
            "opCode": opCode,
            "operandOne": operandOne,
            "operandTwo": operandTwo,
        })

    # Log exit. 
    if mode == 99:
        logger.info({
            "operation": op,
            "opCode": opCode,
            "addr": resultIndex,
        })


if __name__ == "__main__":
    try:
        # Init the logger. 
        logger = init_logger()
        # logger.info({"status": "init"})
        
        # Task one. 
        data = getData(1) 
        parse(data, mode=1, task=1)

        data= getData(2)
        parse(data, mode=1, task=2)

        
    except Exception as e:
        traceback.print_exc()
 
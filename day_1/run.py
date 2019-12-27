'''
@author: Matic Verbic

Solution for https://adventofcode.com/2019/day/1
'''

from math import floor

# Reads data from the provided input file. 
# Returns a list of ints (does no validation). 
def getData():
    with open("/files/day_1/input.txt") as file:
        return [int(line) for line in file]

# Simple mass calculation. 
def calculate_mass(x):
    return x // 3 - 2
        
# Calculates inital mass for each module. 
def calculate_initial_mass(modules):
    return sum([calculate_mass(module) for module in modules])

# Calcualtes mass for each modeule recursively. 
def calculate_mass_recursively(current_mass):
    mass = calculate_mass(current_mass)
    if mass < 0:
        return 0 
    return mass + calculate_mass_recursively(mass)  

# Solves the first task for day one of advent of code. 
def task_1():
    return calculate_initial_mass(getData())

# Solves the second task for day one of advent of code. 
def task_2():
    return sum([calculate_mass_recursively(mass) for mass in getData()])

if __name__ == "__main__":
    print("(task1): Initial mass requires \"{}\" fuel. ".format(task_1()))
    print("(task2): Recursive mass requires \"{}\" fuel. ".format(task_2()))



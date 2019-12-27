'''
@author: Matic Verbic

Solution for https://adventofcode.com/2019/day/3
'''

# Reads data from the provided input file.
def getData():
    with open('/files/day_3/input.txt') as file:
        return [parse(line) for line in file]

# Parses each line.
def parse(line):
    position = [0, 0]
    out = []
    # Parse all commands in a line. 
    for command in line.split(','):
        direction, order = command[0], int(command[1:])

        # Handle each movement. 
        for _ in range(order):
            # Move by 1 vertically
            if direction in ("L", "R"):
                position[1] += 1 if direction in ("U", "R") else -1
                out.append(tuple(position))
                continue        
            
            # Move by 1 horizontally
            position[0] += 1 if direction in ("U", "R") else -1
            out.append(tuple(position))
    
    return out

data = getData()

# Bitwise or to find intersecting points..
intersections = set(data[0]) & set(data[1])

# Quick lambda to find sitance
distance = lambda x, y: abs(x)+abs(y)

if __name__ == "__main__":
    # Find min distance between all intersects. 
    print("(task1): Minimal distance is %d. " % (min([distance(x, y) for (x, y) in intersections])))

    # Find number of intersects for each intersect and return min. 
    result = 2 + min(sum([line.index(intersect) for line in data]) for intersect in intersections)
    print("(task2): Minimal jumps are %d. " % (result)) 
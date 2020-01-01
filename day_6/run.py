from collections import defaultdict

# Gets data from file
def getData(): 
    data = defaultdict(list)
    graph = defaultdict(list)
    with open('/files/day_6/input.txt') as f:
        for row in f:
            planet, orbiter = row.strip().split(')')
            data[planet].append(orbiter)
            graph[planet].append(orbiter)
            graph[orbiter].append(planet)
    return data, graph

# Simple recursive count up of all elements. 
def calculate_paths(current, data):
    if current not in data: 
        return 0
    for orbiter in data[current]:
        return 1 + calculate_paths(orbiter, data)
    
# Implements breadth first approach to parsing a graph. 
def create_paths(start, end, data):
    # Init variables 
    path, visited, queue = {start: 0}, {start}, [start]

    while end not in path:
        # Handle queue. 
        current = queue[0]
        queue = queue[1:]

        for connection in data[current]:
            if connection in visited:
                continue
            
            # Handle an unvisited node. 
            path[connection] = path[current] + 1
            queue = [connection] + queue
            visited.add(connection)

    return path


if __name__ == "__main__":
    # Set up data. 
    data, graph = getData()

    # Task 1
    print("(task1): Number of all orbits is \"{}\". ".format(sum([calculate_paths(planet, data) for planet in data])))

    # Task 2
    print("(task2): Shortest path is \"{}\"".format(create_paths('YOU', 'SAN', graph)["SAN"]-2))
    

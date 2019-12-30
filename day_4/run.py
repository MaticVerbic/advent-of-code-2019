import math 

# Generate numbers. 
def numbers(min, max):
    for i in range(min, max):
        yield i

# Validate the number. 
def validate(number, task):
    # Split the number into a list. 
    split = [(number//(10**i))%10 for i in range(int(math.log(number, 10)), -1, -1)] 

    # Validate length and order. 
    if split != sorted(split) or len(split) != 6: 
        return False
    
    # Validate amount of repeated numbers. 
    doubles = sum([1 if first == second else 0 for first, second in zip(split, split[1:])])

    # If first task exit here. 
    if task == 1: 
        return False if doubles == 0 else True

    # Validate if number contains at least one repeated number of length two.
    counted_doubles = True if [True for i in split if split.count(i) == 2] else False
    
    return False if doubles == 0 or not counted_doubles else True

# Count up validated numbers. 
count_one, count_two = 0, 0
for number in numbers(264793, 803935):
    count_one += 1 if validate(number, 1) else 0
    count_two += 1 if validate(number, 2) else 0

# Output 
print("(task1): There are \"{}\" possible passwords. ".format(count_one))
print("(task2): There are \"{}\" possible passwords. ".format(count_two))

import os
import sys

if len(sys.argv) != 2: 
    print("invalid argument count")
    exit(2)

if sys.argv[1] == "run": 
    for item in os.listdir('.'):
        if os.path.isdir(item) and "day_" in item:
            print("Day {}:".format(item.split("_")[1]))
            os.system('python3 /files/{}/run.py'.format(item))


if sys.argv[1] == "test": 
    for item in os.listdir('.'):
        if os.path.isdir(item) and "day_" in item:
            if not os.path.exists("/files/{}/run_test.py".format(item)):
                continue 
            print("Day {}:".format(item.split("_")[1]))
            os.system('python3 /files/{}/run_test.py'.format(item))

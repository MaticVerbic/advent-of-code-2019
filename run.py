import os

for item in os.listdir('.'):
    if os.path.isdir(item) and "day_" in item:
        print("Day %s:" % (item.split("_")[1]))
        os.system('python3 /files/%s/run.py' % item)
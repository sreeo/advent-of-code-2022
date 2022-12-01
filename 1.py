from collections import defaultdict

def def_value():
    return 0

f = open("input/1.txt", "r")
index = 0
map = defaultdict(def_value)
calories = []

max_total = 0
while True:
    line = f.readline()
    if not line:
        break
    line = line.strip()
    if line:
        if len(calories)-1 < index:
            calories.append(int(line))
        else:
            calories[index] += int(line)
    else:
        index += 1
calories.sort(reverse=True)  

print(calories[0])
print(calories[0] + calories[1] + calories[2])

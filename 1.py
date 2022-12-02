f = open("input/1.txt", "r")
index = 0
calories = []

max_total = 0
while True:
    line = f.readline()

    if not line:
        break
    line = line.strip()

    if line:
        if len(calories) - 1 < index:
            calories.append(int(line))
        else:
            calories[index] += int(line)
    else:
        index += 1
f.close()

calories.sort(reverse=True)

print(calories[0])
print(calories[0] + calories[1] + calories[2])

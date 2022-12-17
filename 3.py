f = open("input/3.txt", "r")
index = 0
sum_of_priority = 0

max_total = 0

def get_priority(char):
    to_subtract = 64 - 26

    if ord(char) > 96:
        to_subtract = 96
    return ord(char) - to_subtract

while True:
    common_char = []

    line = f.readline()

    if not line:
        break
    line = line.strip()

    items = list(line)
    first_part = items[:int(len(items)/2)]
    second_part = items[int(len(items)/2):]

    for i in first_part:
        if i in second_part:
            common_char.append(i)

    common_char = list(set(common_char))

    for i in common_char:
        sum_of_priority += get_priority(i)

f.close()
print(sum_of_priority)

f = open("input/3.txt", "r")
group = []
sum_of_priority = 0
common_char = []

while True:
    index+= 1

    line = f.readline()

    if not line:
        break
    line = line.strip()
    group.append(line)

    if len(group) % 3 == 0:
        first_rucksack = group[0]
        second_rucksack = group[1]
        third_rucksack = group[2]

        for i in first_rucksack:
            if i in second_rucksack and i in third_rucksack:
                common_char.append(i)

        common_char = list(set(common_char))
        for i in common_char:
            sum_of_priority += get_priority(i)
        common_line = ""
        common_char = []
        group = []
    
    
f.close()
print("second part")
print(sum_of_priority)
import re
f = open("input/5.txt", "r")
index = 0
calories = []
matrix = []

max_total = 0
while True:
    line = f.readline()

    if not line:
        break
    line = line.strip()

    stack_position_match = re.findall(r"(\s{1,4})*(\[[A-Z]\])", line)
    current_row_res = ['', '', '']
    print(stack_position_match)
    if stack_position_match:
        for index, i in enumerate(stack_position_match):
            for val in i:
                if val or val in [" "]:
                    val = val.replace("[", "")
                    val = val.replace("]", "")
                    current_row_res[index] = val

        matrix.append(current_row_res)

f.close()
print(matrix)

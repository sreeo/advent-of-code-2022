f = open("input/4.txt", "r")

count_of_inclusion = 0
count_of_overlap = 0
while True:
    line = f.readline()

    if not line:
        break
    line = line.strip()

    assignments = line.split(",")
    dictionary = {}
    first_assignment_lower_limit = int(assignments[0].split("-")[0])
    first_assignment_upper_limit = int(assignments[0].split("-")[1])

    second_assignment_lower_limit = int(assignments[1].split("-")[0])
    second_assignment_upper_limit = int(assignments[1].split("-")[1])


    if first_assignment_lower_limit < second_assignment_lower_limit or first_assignment_upper_limit > second_assignment_upper_limit:
        first_tuple = (first_assignment_lower_limit, first_assignment_upper_limit)
        second_tuple = (second_assignment_lower_limit, second_assignment_upper_limit)
    else:
        first_tuple = (second_assignment_lower_limit, second_assignment_upper_limit)
        second_tuple = (first_assignment_lower_limit, first_assignment_upper_limit)

    if second_tuple[0] >= first_tuple[0] and second_tuple[1] <= first_tuple[1]:
        count_of_inclusion += 1
    
    range_tuple = range(first_tuple[0], first_tuple[1] + 1)

    if second_tuple[0] in range_tuple or second_tuple[1] in range_tuple:
        count_of_overlap += 1

print(count_of_inclusion)
print(count_of_overlap)
f.close()


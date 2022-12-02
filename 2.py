score_map = {"rock": 1, "paper": 2, "scissor": 3}

opponent_map = {
    "A": "rock",
    "B": "paper",
    "C": "scissor"
}

move_map1 = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissor"
}

result_map = {
    "rock" : "scissor",
    "paper" : "rock",
    "scissor" : "paper"
}


def process_result_part1(opponent_move, personal_move):
    opponent_move = opponent_map[opponent_move]
    personal_move = move_map1[personal_move]

    if opponent_move == personal_move:
        score = 3

    elif result_map[personal_move] == opponent_move:
        score = 6
    else:
        score = 0
    
    score += score_map[personal_move]
    return score

def process_result_part2(opponent_move, result):
    opponent_move = opponent_map[opponent_move]

    if result == "Y":
        personal_move = opponent_move
        score = 3
    elif result == "X":
        personal_move = result_map[opponent_move]
        score = 0
    else:
        personal_move = list({i for i in result_map if result_map[i] == opponent_move})
        personal_move = personal_move[0]

        score = 6
    score += score_map[personal_move]
    return score

total_score = 0
total_score2 = 0

with open("input/2.txt", "r") as f:

    for line in f:
        line = line.strip()
        moves = line.split(" ")
        total_score += process_result_part1(moves[0], moves[1])
        total_score2 += process_result_part2(moves[0], moves[1])

print(total_score)
print(total_score2)
import random


def create_return_match(match_schedule):
    for current_round in match_schedule:
        for current_match in current_round:
            team = current_match.pop(1)
            current_match.insert(0, team)
        random.shuffle(current_round)
    return match_schedule


teams = list(range(4))
# check if teams are odd or not
if len(teams) % 2 != 0:
    print("Số lượng teams phải là số chẵn")
    exit()
random.shuffle(teams)

num_of_rounds = len(teams) - 1
num_of_matches_per_round = len(teams) // 2

match_schedule = []

# create round
for i in range(num_of_rounds):
    round = []

    # create matches per round
    for j in range(num_of_matches_per_round):
        if i % 2 == 0:
            match = [teams[j], teams[-(j+1)]]
        else:
            match = [teams[-(j+1)], teams[j]]

        # add match to round
        round.append(match)

    # shuffle matches per round
    random.shuffle(round)

    # add round to match_schedule
    match_schedule.append(round)

    # rearrange teams to create new round
    x = teams.pop(num_of_rounds)
    teams.insert(2, x)

print("Lượt đi")
for round in match_schedule:
    print(round)

return_matches = create_return_match(match_schedule)
print("Lượt về")
for round in return_matches:
    print(round)

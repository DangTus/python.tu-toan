import random


############### biến toàn cục ###############

list_team = [i for i in range(0, 3)]

if len(list_team) % 2 != 1:
    print('--- Error: Tổng số lượng các đội phải là số lẻ ---')
    exit()

len_row = len(list_team)//2
len_match_in_row = len(list_team)

create_matches = []
for i in range(len(list_team)):
    for j in range(i+1, len(list_team)):
        if (i+j) % 2 == 0:
            create_matches.append([list_team[i], list_team[j]])
        else:
            create_matches.append([list_team[j], list_team[i]])

############### biến toàn cục ###############


def check_team_in_round(team_check, round_check):
    count = 0

    for match in round_check:
        if team_check in match:
            count += 1

    if count > 1:
        return False
    else:
        return True


def sort_match_in_away_round(round):
    while True:
        list_team_copy = list_team[:]
        match_middle = round[len(round)//2]

        for match in round[:len(round)//2]:
            for team in match:
                if team in list_team_copy:
                    list_team_copy.remove(team)

        if len(list_team_copy) == 1 and list_team_copy[0] in match_middle and (round[0][0] in match_middle or round[0][1] in match_middle):
            return round
        else:
            random.shuffle(round)


def shuffle_match_in_round(round_list):
    for round in round_list:
        random.shuffle(round)

    return round_list


def create_away_rounds():
    away_rounds = []
    list_all_match = create_matches[:]

    while len(away_rounds) < len_row:
        round = []

        while len(round) < len_match_in_row:
            random.shuffle(list_all_match)
            reset = True

            for match in list_all_match:
                if check_team_in_round(match[0], round) and check_team_in_round(match[1], round):
                    round.append(match)
                    list_all_match.remove(match)
                    reset = False

                    break

            if reset:
                away_rounds.clear()
                round.clear()
                list_all_match = create_matches[:]
                print('reset thanh cong')

        round = sort_match_in_away_round(round)
        away_rounds.append(round[:])

    return away_rounds


def create_home_rounds(rounds_away):    
    home_rounds = []

    for round in rounds_away:
        round_new = []
        for match in round:
            round_new.append(match[::-1])

        random.shuffle(round_new)
        round_new = sort_match_in_away_round(round_new)
        home_rounds.append(round_new)

    return home_rounds


away_rounds = create_away_rounds()
print('\n--- Lượt đi ---')
for x in away_rounds:
    print(x)

home_rounds = create_home_rounds(away_rounds)
print('\n--- Lượt về ---')
for x in home_rounds:
    print(x)

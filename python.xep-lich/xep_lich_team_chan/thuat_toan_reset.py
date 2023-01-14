import random


############### biến toàn cục ###############

list_team = [i for i in range(0, 10)]

if len(list_team) % 2 != 0:
    print('--- Error: Tổng số lượng các đội phải là số chẵn ---')
    exit()

len_row = len(list_team)-1
len_match_in_row = len(list_team)//2

create_matches = []
for i in range(len(list_team)):
    for j in range(i+1, len(list_team)):
        if (i+j) % 2 == 0:
            create_matches.append([list_team[i], list_team[j]])
        else:
            create_matches.append([list_team[j], list_team[i]])

############### biến toàn cục ###############


def check_match(match_check, round):
    all_teams = [team for match in round for team in match]
    return all(team not in all_teams for team in match_check)


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
                if check_match(match, round):
                    round.append(match)
                    list_all_match.remove(match)
                    reset = False

                    break

            if reset:
                away_rounds.clear()
                round.clear()
                list_all_match = create_matches[:]
                print('reset thanh cong')

        away_rounds.append(round)

    return shuffle_match_in_round(away_rounds)


def create_home_rounds(rounds_away):
    return shuffle_match_in_round([[match[::-1] for match in round] for round in rounds_away])


away_rounds = create_away_rounds()
print('\n--- Lượt đi ---')
for x in away_rounds:
    print(x)

home_rounds = create_home_rounds(away_rounds)
print('\n--- Lượt về ---')
for x in home_rounds:
    print(x)

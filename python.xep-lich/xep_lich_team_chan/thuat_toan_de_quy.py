import random


############### biến toàn cục ###############

list_team = [i for i in range(0, 10)]

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


class Schedule:
    def __init__(self, round_list: list, round_wrong_list: list):
        # list lịch đấu
        self.round_list = round_list
        # list lịch đấu đã tìm nhưng sai
        self.round_wrong_list = round_wrong_list

    # method
    def find_remaining_matches(self):
        round_matches = [match for round in self.round_list for match in round]
        return [match for match in create_matches if match not in round_matches]

    def create_round(self):
        remaining_matches = self.find_remaining_matches()
        round = []

        while len(round) < len_match_in_row:
            random.shuffle(remaining_matches)
            find = False

            for match in remaining_matches:

                if check_match(match, round):
                    round.append(match)
                    remaining_matches.remove(match)
                    find = True
                    break

            if not find:
                return False

        return round

    def add_round_wrong(self):
        round_wrong = self.round_list[-1]

        self.round_list.remove(round_wrong)
        self.round_wrong_list.append(round_wrong[:])


def create_schedule(list_round: list, list_round_wrong: list):
    # Kiểm tra xem đã đủ vòng đấu hay chưa
    if len(list_round) == len_row:
        return list_round

    # Tạo class lịch đấu
    schedule = Schedule(list_round, list_round_wrong)

    # Kiểm tra xem list các vòng đấu sai đã đầy chưa
    found_matches = len(schedule.round_wrong_list)
    remaining_matches = len(schedule.find_remaining_matches())
    if found_matches == remaining_matches*100:
        return False

    # Tạo vòng đấu mới
    round = schedule.create_round()

    # Kiểm tra xem vòng đấu có hợp lệ hay không và có ở trong list các vòng đấu sai hay không
    if round:
        if round not in schedule.round_wrong_list:
            schedule.round_list.append(round[:])

            round_list = create_schedule(schedule.round_list, [])
            if (round_list):
                return round_list
            else:
                schedule.add_round_wrong()
                return create_schedule(schedule.round_list, schedule.round_wrong_list)
        else:
            return create_schedule(schedule.round_list, schedule.round_wrong_list)
    else:
        return False


list_lich_dau = create_schedule([], [])

if list_lich_dau:
    for x in list_lich_dau:
        print(x)
else:
    print('khong the sap xep lich dau')

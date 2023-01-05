import random


def check_vong_dau(team: str, vong_dau: list):
    if not vong_dau:
        return False
    else:
        for item in vong_dau:
            team_trong_vong_dau = item.split('-')
            if team in team_trong_vong_dau:
                return True

        return False


def check_lich_dau(team1, team2):
    if not lich_dau:
        return False
    else:
        for vong_dau in lich_dau:
            kiem_tra1 = team1 + '-' + team2
            kiem_tra2 = team2 + '-' + team1

            if kiem_tra1 in vong_dau or kiem_tra2 in vong_dau:
                return True

        return False


teams = ['1', '2', '3', '4', '5', '6']

so_vong_dau = len(teams)-1
so_tran_moi_vong = len(teams)//2

lich_dau = []

while len(lich_dau) != so_vong_dau:
    vong_dau = []

    while len(vong_dau) != so_tran_moi_vong:
        dem = 0
        while True:
            team1 = random.choice(teams)

            while True:
                team2 = random.choice(teams)
                if (team1 != team2):
                    break

            if not check_vong_dau(team1, vong_dau) and not check_vong_dau(team2, vong_dau) and not check_lich_dau(team1, team2):
                break

            if dem < 50:
                dem += 1
            else:
                lich_dau.clear()
                vong_dau.clear()
                dem = 0

        vong_dau.append(team1 + '-' + team2)

    lich_dau.append(vong_dau)

for iii in lich_dau:
    print(iii)

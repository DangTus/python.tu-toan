import random


def check_vong_dau(m, vong):
    if not vong:
        return False
    else:
        for tran_dau_trong_vong in vong:
            for team in m:
                if team in tran_dau_trong_vong:
                    return True
        return False


teams = [i for i in range(1, 21)]

so_vong_dau = len(teams)-1
so_tran_moi_vong = len(teams)//2

# tạo các trận đấu
matchs = []
for i in range(len(teams)):
    for j in range(i+1, len(teams)):
        matchs.append([teams[i], teams[j]])

so_lan_tim_team_random = len(matchs) * 2

lich_dau = []

while len(lich_dau) != so_vong_dau:
    vong_dau = []

    while len(vong_dau) != so_tran_moi_vong:
        dem = 0

        while True:
            match = random.choice(matchs)
            if not check_vong_dau(match, vong_dau):
                break

            if dem <= so_lan_tim_team_random:
                dem += 1
            else:
                lich_dau.clear()
                vong_dau.clear()
                dem = 0

        vong_dau.append(match)

    lich_dau.append(vong_dau)

for vong in lich_dau:
    print(vong)

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


def show_match_by_team(team):
    for vong in lich_dau:
        for tran in vong:
            if team in tran:
                print(tran)


teams = [i for i in range(0, 6)]

so_vong_dau = len(teams)-1
so_tran_moi_vong = len(teams)//2

# tạo các trận đấu
matchs_root = []
for i in range(len(teams)):
    for j in range(i+1, len(teams)):
        if (i+j) % 2 == 0:
            matchs_root.append([teams[i], teams[j]])
        else:
            matchs_root.append([teams[j], teams[i]])

matchs = matchs_root[:]
print(matchs_root)

lich_dau = []

while len(lich_dau) < so_vong_dau:
    vong_dau = []

    while len(vong_dau) < so_tran_moi_vong:
        random.shuffle(matchs)

        reset = True
        for match in matchs:
            if not check_vong_dau(match, vong_dau):
                vong_dau.append(match)
                matchs.remove(match)

                reset = False
                break

        if reset:
            lich_dau.clear()
            vong_dau.clear()
            matchs = matchs_root[:]
            print('reset thanh cong')

    lich_dau.append(vong_dau)

for vong in lich_dau:
    print(vong)


show_match_by_team(0)

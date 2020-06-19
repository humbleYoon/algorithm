# 동: 1, 서: 2, 남: 3, 북: 4
# 4 2 3 1 3 1 -> 1: 2개, 2: 1개, 3: 2개, 4: 1개
# 4 2 3 1 4 1 -> 1: 2개, 2: 1개, 3: 1개, 4: 2개
# 4 2 4 2 3 1 -> 1: 1개, 2: 2개, 3: 1개, 4: 2개
# 4 2 3 2 3 1 -> 1: 1개, 2: 2개, 3: 2개, 4: 1개

melonNum = int(input())
dnum_list = [0, 0, 0, 0, 0]
info_list = []
for i in range(6):
    direction, length = map(int, input().split())
    info_list.append([direction, length])
    dnum_list[direction] += 1
wh_list = []
for i in range(5):
    if dnum_list[i] == 1:
        wh_list.append(i)

result = 1
for i in range(2):
    for j in range(6):
        if wh_list[i] == info_list[j][0]:
            result *= info_list[j][1]

temp_multi = 1
idx = -1
if dnum_list[1] == 2 and dnum_list[3] == 2:
    for i in range(6):
        if 2 == info_list[i][0]:
            idx = i
elif dnum_list[1] == 2 and dnum_list[4] == 2:
    for i in range(6):
        if 3 == info_list[i][0]:
            idx = i
elif dnum_list[2] == 2 and dnum_list[4] == 2:
    for i in range(6):
        if 1 == info_list[i][0]:
            idx = i
elif dnum_list[2] == 2 and dnum_list[3] == 2:
    for i in range(6):
        if 4 == info_list[i][0]:
            idx = i
temp_multi *= info_list[(idx+2)%6][1]
temp_multi *= info_list[(idx+3)%6][1]
print("{0}".format((result-temp_multi)*melonNum))
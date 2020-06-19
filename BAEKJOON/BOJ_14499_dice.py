dx = [0, 0, -1, 1]
dy = [1, -1, 0 , 0]

nmxyk_list = list(map(int, input().split(" ")))
N = nmxyk_list[0]
M = nmxyk_list[1]
start_x = nmxyk_list[2]
start_y = nmxyk_list[3]
k = nmxyk_list[4]
dice_map = [[0 for i in range(20)] for j in range(20)]

dice_status = [0, 0, 0, 0, 0, 0, 0]

# [1] = 아래, [2] = 앞, [3] = 오른쪽, [4] = 왼쪽, [5] = 뒷, [6] = 위
# 북으로 이동 : [1] = [2], [2] = [6], [6] = [5], [5] = [1]
# 동 : [1] = [3], [3] = [6], [6] = [4], [4] = [1]
# 남 : [1] = [5], [5] = [6], [6] = [2], [2] = [1]
# 서 : [1] = [4], [4] = [6], [6] = [3], [3] = [1]

for i in range(N):
    map_list = list(map(int, input().split(" ")))
    for j in range(M):
        dice_map[i][j] = map_list[j]

direction_list = list(map(int, input().split(" ")))
for i in direction_list:
    if start_x + dx[i-1] < 0 or start_x + dx[i-1] >= N or start_y + dy[i-1] < 0 or start_y + dy[i-1] >= M:
        continue

    if i == 1:
        start_y += 1
        temp = dice_status[1]
        dice_status[1] = dice_status[3]
        dice_status[3] = dice_status[6]
        dice_status[6] = dice_status[4]
        dice_status[4] = temp
    elif i == 2:
        start_y += -1
        temp = dice_status[1]
        dice_status[1] = dice_status[4]
        dice_status[4] = dice_status[6]
        dice_status[6] = dice_status[3]
        dice_status[3] = temp
    elif i == 3:
        start_x += -1
        temp = dice_status[1]
        dice_status[1] = dice_status[2]
        dice_status[2] = dice_status[6]
        dice_status[6] = dice_status[5]
        dice_status[5] = temp
    else:
        start_x += +1
        temp = dice_status[1]
        dice_status[1] = dice_status[5]
        dice_status[5] = dice_status[6]
        dice_status[6] = dice_status[2]
        dice_status[2] = temp

    if dice_map[start_x][start_y] == 0:
        dice_map[start_x][start_y] = dice_status[1]
    else:
        dice_status[1] = dice_map[start_x][start_y]
        dice_map[start_x][start_y] = 0

    print(dice_status[6])
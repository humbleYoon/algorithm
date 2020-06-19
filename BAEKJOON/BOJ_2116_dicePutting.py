CONST_INT_MAX = 10005
dice_list = [[0 for i in range(6)] for j in range(CONST_INT_MAX)]

dice_num = int(input())
for i in range(dice_num):
    dice_list[i][0], dice_list[i][1], dice_list[i][2], dice_list[i][3], dice_list[i][4], dice_list[i][5] = map(int, input().split())

result = -9979871284
pair_list = [5, 3, 4, 1, 2, 0]
for i in range(6):
    temp_result = 0
    down = dice_list[0][i]
    up = dice_list[0][pair_list[i]]
    dice_max = -98867237123
    for j in range(6):
        if j == i or j == pair_list[i]:
            continue
        if dice_list[0][j] > dice_max:
            dice_max = dice_list[0][j]
    temp_result += dice_max
    
    for j in range(dice_num-1):
        dice_max = -989781623
        for k in range(6):
            if up == dice_list[j+1][k]:
                down_idx = k
                up = dice_list[j+1][pair_list[down_idx]]
                break
        for k in range(6):
            if k == down_idx or k == pair_list[down_idx]:
                continue
            if dice_list[j+1][k] > dice_max:
                dice_max = dice_list[j+1][k]
        temp_result += dice_max

    if temp_result > result:
        result = temp_result

print(result)
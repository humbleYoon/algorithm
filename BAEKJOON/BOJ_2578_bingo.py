map_list = []
for i in range(5):
    row_list = list(map(int, input().split()))
    map_list.append(row_list)
callOrder = []
for i in range(5):
    n1, n2, n3, n4, n5 = map(int, input().split())
    callOrder.append(n1)
    callOrder.append(n2)
    callOrder.append(n3)
    callOrder.append(n4)
    callOrder.append(n5)

for i in range(25):
    for j in range(5):
        for k in range(5):
            if callOrder[i] == map_list[j][k]:
                map_list[j][k] = 0
    
    bingo_num = 0
    for j in range(5):
        if map_list[j][0] == 0 and map_list[j][1] == 0 and map_list[j][2] == 0 and map_list[j][3] == 0 and map_list[j][4] == 0:
            bingo_num += 1
        if map_list[0][j] == 0 and map_list[1][j] == 0 and map_list[2][j] == 0 and map_list[3][j] == 0 and map_list[4][j] == 0:
            bingo_num += 1
    if map_list[0][0] == 0 and map_list[1][1] == 0 and map_list[2][2] == 0 and map_list[3][3] == 0 and map_list[4][4] == 0:
        bingo_num += 1
    if map_list[4][0] == 0 and map_list[3][1] == 0 and map_list[2][2] == 0 and map_list[1][3] == 0 and map_list[0][4] == 0:
        bingo_num += 1

    if bingo_num >= 3:
        print("{0}".format(i+1))
        break
import sys

sys.stdin = open('input_3.txt', 'r')

import time

T = int(input())
for test_case in range(T):
    st = time.time()
    N, M, C = map(int, input().split())
    map_list = []
    for i in range(N):
        temp_list = list(map(int, input().split()))
        map_list.append(temp_list)
    mineral_position = []
    mineral_weightCost = []
    mineral_num = 0
    for i in range(N):
        for j in range(M):
            if map_list[i][j] == 1:
                robot_pos_x = i
                robot_pos_y = j
            elif map_list[i][j] > 1:
                mineral_position.append([i, j])
                mineral_num += 1
    for i in mineral_position:
         mineral_weightCost.append([map_list[i[0]][i[1]], 2*(abs(robot_pos_x-i[0])+abs(robot_pos_y-i[1]))])
    
    result = 0
    Table = [[] for i in range(mineral_num)]
    for i in range(mineral_num):
        # T[n] = n을 마지막으로 들릴 때 얻을 수 있는 미네랄의 양과 코스트의 경우의 수
        if i == 0:
            if C >= mineral_weightCost[i][1]:
                Table[i].append([mineral_weightCost[i][0], C-mineral_weightCost[i][1]])
                if mineral_weightCost[i][0] > result:
                    result = mineral_weightCost[i][0]
            Table[i].append([0, C])
        else:
            for j in range(0, i):
                for k in Table[j]:
                    if k[1] >= mineral_weightCost[i][1]:
                        Table[i].append([k[0]+mineral_weightCost[i][0], k[1]-mineral_weightCost[i][1]])
                        if k[0]+mineral_weightCost[i][0] > result:
                            result = k[0]+mineral_weightCost[i][0]
    
    print("#{0} {1}".format(test_case+1, result))
    print(time.time() - st)
                    
# 맵을 기준으로 본다면? '1000*1000 = 백만' x 'K=300' = 3억. -> 불가
# 각 시간의 활성 상태, 비활성, 죽을 상태 리스트를 만듦 -> 900개
# 시간을 하나씩 지나면서 각 시간의 활성, 비활성, 죽을 상태 리스트, 맵을 통해,
# 이후 시간의 활성, 비활성, 죽을 상태 리스트와 맵 상태를 제어해주고, 죽은 상태는 맵에서 -1로 변화
# 맨 마지막 시간이 끝나고 맵에서 0, -1 제외하고 카운팅해서 구함

# 1. 비활성 상태 -> 이후의 활성 상태와 죽을 상태, 맵을 제어한다.
# 2. 활성 상태 -> 이후의 비활성 상태를 제어한다.
# 3. 죽을 상태 -> 죽여주면서 맵을 제어한다.

# 맵의 기준점은 (400, 400)
CONST_INT_MAX = 800

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for test_case in range(T):
    N, M, K = map(int, input().split())
    map_list = [[0 for i in range(CONST_INT_MAX)] for j in range(CONST_INT_MAX)]
    die_list = [[] for i in range(K + 15)]
    act_list = [[] for i in range(K + 15)]
    preact_list = [[] for i in range(K + 15)]  # x, y, 생명력
    for i in range(N):
        row_list = list(map(int, input().split()))
        for j in range(M):
            map_list[400 + i][400 + j] = row_list[j]
            if map_list[400 + i][400 + j] > 0:
                preact_list[0].append([400 + i, 400 + j, map_list[400 + i][400 + j]])

    for i in range(K + 1):  # i는 시간
        for j in preact_list[i]:
            act_list[i + j[2]].append([j[0], j[1], j[2]])
            die_list[i + j[2] * 2].append([j[0], j[1], j[2]])
            map_list[j[0]][j[1]] = j[2]

        temp_list = []  # x, y, 생명력
        for j in act_list[i]:
            for k in range(4):
                mx = j[0] + dx[k]
                my = j[1] + dy[k]
                if map_list[mx][my] != 0:
                    continue

                temp_idx = -1
                for l in range(len(temp_list)):
                    if temp_list[l][0] == mx and temp_list[l][1] == my:
                        temp_idx = l
                        break

                if temp_idx != -1:
                    if temp_list[temp_idx][2] < map_list[j[0]][j[1]]:
                        temp_list[temp_idx][2] = map_list[j[0]][j[1]]
                else:
                    temp_list.append([mx, my, map_list[j[0]][j[1]]])

        for j in temp_list:
            preact_list[i + 1].append([j[0], j[1], j[2]])

        for j in die_list[i]:
            map_list[j[0]][j[1]] = -1

    result = 0
    for i in range(CONST_INT_MAX):
        for j in range(CONST_INT_MAX):
            if map_list[i][j] >= 1:
                result += 1

    print("#{0} {1}".format(test_case + 1, result))

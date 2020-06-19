T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def room_DFS(x, y):
    global distance, N
    global map_info, each_Max
    
    if distance <= each_Max[x][y]:
        return None
    each_Max[x][y] = distance
    
    for i in range(4):
        if x+dx[i] < 0 or x+dx[i] >= N or y+dy[i] < 0 or y+dy[i] >= N:
            continue
        if map_info[x+dx[i]][y+dy[i]]-1 == map_info[x][y]:
            distance += 1
            room_DFS(x+dx[i], y+dy[i])
            break


for test_case in range(T):
    N = int(input())
    map_info = []
    for i in range(N):
        map_info.append(list(map(int, input().split())))
    each_Max = [[0 for i in range(N)] for j in range(N)]
    result = -9861233
    result_room = -1

    for i in range(N):
        for j in range(N):
            distance = 1
            room_DFS(i, j)
            if result < distance:
                result = distance
                result_room = map_info[i][j]
            elif result == distance:
                if result_room > map_info[i][j]:
                    result_room = map_info[i][j]

    print("#{0} {1} {2}".format(test_case+1, result_room, result))
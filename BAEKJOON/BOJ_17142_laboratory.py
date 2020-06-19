import itertools, collections

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
map_info = []
virus_info = []
zero_cnt = 0
for i in range(N):
    temp_list = list(map(int, input().split()))
    map_info.append(temp_list)
    for j in range(len(temp_list)):
        if temp_list[j] == 2:
            virus_info.append([i, j])
        elif temp_list[j] == 0:
            zero_cnt += 1
select_info = list(itertools.combinations(virus_info, M))
result = 3000

for i in select_info:
    temp_zero_cnt = zero_cnt
    q = collections.deque([])
    visited = [[False for j in range(N)] for k in range(N)]
    for j in i:
        visited[j[0]][j[1]] = True
        q.append([j[0], j[1]])
    temp_time = 0
    flag = True
    while q:
        length = len(q)
        for j in range(length):
            current = q.popleft()
            for k in range(4):
                nx = current[0] + dx[k]
                ny = current[1] + dy[k]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if temp_zero_cnt > 0:
                    if (map_info[nx][ny] == 0 or map_info[nx][ny] == 2) and visited[nx][ny] == False:
                        if map_info[nx][ny] == 0:
                            temp_zero_cnt -= 1
                        visited[nx][ny] = True
                        q.append([nx, ny])
        if len(q) == 0:
            break
        temp_time += 1
    for j in range(N):
        for k in range(N):
            if map_info[j][k] == 0 and visited[j][k] == False:
                flag = False
    if flag == True:
        if result > temp_time:
            result = temp_time
if result == 3000:
    print("-1")
else:
    print("{0}".format(result))

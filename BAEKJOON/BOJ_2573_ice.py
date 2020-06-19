# 완전탐색 돌면서 빙산의 높이 조절해주고, 새로운 맵에 추가시켜줘야 함
# DFS 혹은 BFS로 두 개로 나눠지는지 확인
import collections

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
map_list = []
for i in range(N):
    row_list = list(map(int, input().split()))
    map_list.append(row_list)

result = 0
temp_list = [[0 for i in range(M)] for j in range(N)]
while True:
    visited = [[False for i in range(M+5)] for j in range(N+5)]
    result += 1
    for i in range(N):
        for j in range(M):
            if map_list[i][j] != 0:
                cnt = 0
                for k in range(4):
                    mx = i + dx[k]
                    my = j + dy[k]
                    if mx < 0 or mx >= N or my < 0 or my >= M:
                        continue
                    if map_list[mx][my] == 0:
                        cnt += 1
                if map_list[i][j] - cnt > 0:
                    temp_list[i][j] = map_list[i][j] - cnt
                else:
                    temp_list[i][j] = 0
            else:
                temp_list[i][j] = 0
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if temp_list[i][j] != 0 and visited[i][j] == False:
                cnt += 1
                myQueue = collections.deque([])
                visited[i][j] = True
                myQueue.append([i, j])
                while myQueue:
                    current = myQueue.popleft()
                    for k in range(4):
                        mx = current[0] + dx[k]
                        my = current[1] + dy[k]
                        if mx < 0 or mx >= N or my < 0 or my >= M:
                            continue
                        if visited[mx][my] == False and temp_list[mx][my] != 0:
                            visited[mx][my] = True
                            myQueue.append([mx, my])
    
    if cnt >= 2:
        print("{0}".format(result))
        break
    elif cnt == 0:
        print("0")
        break

    for i in range(N):
        for j in range(M):
            map_list[i][j] = temp_list[i][j]
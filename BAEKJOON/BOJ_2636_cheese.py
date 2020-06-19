# 1. 경계선 부분은 무조건 치즈 -> 경계선에서 DFS 해서 들어간 곳은 전부 공기(2)로 처리
# 2. 치즈 부분 DFS 하면서(치즈 개수 새야함) 녹을 부분 처리(녹는 부분 새야함) -> DFS 다 돌고 해당 좌표 2로 바꿔줌
# 3. 위 행위 반복하면서 반복 횟수 카운팅 하고, 치즈 개수 == 녹는 부분 개수 같아지면 다 녹은거니까 스탑하고, 치즈 개수 출력
# *파이썬 재귀호출 제한이 깊이 기준 1000번이기 때문에 sys.setrecursionlimit 필요하고, 삼성 코테에서는 사용 불가
# *때문에 이차원 배열을 탐색해야 하는 경우에는 BFS로 도는 것이 좋다(맵 크기가 1000을 넘어갈 경우)
# *백트래킹은 깊이가 작기 때문에 상관 없음

import sys
sys.setrecursionlimit(100000)

CONST_INT_MAX = 105

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def air_DFS(x, y):
    global visited
    global height
    global width
    global map_list
    
    visited[x][y] = True
    map_list[x][y] = 2

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if mx < 0 or mx >= height or my < 0 or my >= width:
            continue
        if visited[mx][my] == False and (map_list[mx][my] == 0 or map_list[mx][my] == 2):
            air_DFS(mx, my)

def cheese_DFS(x, y):
    global visited
    global height
    global width
    global map_list
    global melt_list
    global cheese_num
    global melt_num

    cheese_num += 1
    visited[x][y] = True

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if mx < 0 or mx >= height or my < 0 or my >= width:
            continue
        if map_list[mx][my] == 2:
            melt_list.append([x, y])
            melt_num += 1
            break

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if mx < 0 or mx >= height or my < 0 or my >= width:
            continue
        if visited[mx][my] == False and map_list[mx][my] == 1:
            cheese_DFS(mx, my)


height, width = map(int, input().split())
map_list = []
for i in range(height):
    row_list = list(map(int, input().split()))
    map_list.append(row_list)

cnt = 0
while True:
    cnt += 1
    visited = [[False for i in range(CONST_INT_MAX)] for j in range(CONST_INT_MAX)]

    for i in range(height):
        for j in range(width):
            if i == 0 or j == 0 or i == height-1 or j == width-1:
                if visited[i][j] == False and (map_list[i][j] == 0 or map_list[i][j] == 2):
                    air_DFS(i, j)
    
    melt_list = []
    cheese_num = 0
    melt_num = 0
    for i in range(height):
        for j in range(width):
            if visited[i][j] == False and map_list[i][j] == 1:
                cheese_DFS(i, j)

    if cheese_num == melt_num:
        print("{0}".format(cnt))
        print("{0}".format(cheese_num))
        break
    else:
        for i in melt_list:
            map_list[i[0]][i[1]] = 2
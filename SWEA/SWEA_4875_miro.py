CONST_INT_MAX = 105

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def miro_dfs(x, y):
    global N
    global map_info
    global visited
    global result

    visited[x][y] = True
    if map_info[x][y] == '3':
        result = 1

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if mx < 0 or mx >= N or my < 0 or my >= N:
            continue
        if map_info[mx][my] != '1' and visited[mx][my] == False:
            miro_dfs(mx, my)

T = int(input())
for test_case in range(T):
    N = int(input())
    map_info = []
    visited = [[False for i in range(CONST_INT_MAX)] for j in range(CONST_INT_MAX)]
    result = 0
    for i in range(N):
        row_info = input()
        map_info.append(row_info)
    
    for i in range(N):
        for j in range(N):
            if map_info[i][j] == '2':
                start_x = i
                start_y = j

    miro_dfs(start_x, start_y)
    print("#{0} {1}".format(test_case+1, result))

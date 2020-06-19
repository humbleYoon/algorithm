CONST_INT_MAX = 105

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for test_case in range(T):
    N = int(input())
    map_str = []
    myQueue = []
    visited = [[False for i in range(CONST_INT_MAX)] for j in range(CONST_INT_MAX)]
    for i in range(N):
        row_str = input()
        map_str.append(row_str)
    for i in range(N):
        for j in range(N):
            if map_str[i][j] == '2':
                start_x = i
                start_y = j
    
    visited[start_x][start_y] = True
    myQueue.append([start_x, start_y])
    distance = 0
    flag = False
    while myQueue:
        q_length = len(myQueue)
        for i in range(q_length):
            current = myQueue.pop(0)
            if map_str[current[0]][current[1]] == '3':
                flag = True
                break
            for j in range(4):
                mx = current[0] + dx[j]
                my = current[1] + dy[j]
                if mx < 0 or mx >= N or my < 0 or my >= N:
                    continue
                if visited[mx][my] == False and map_str[mx][my] != '1':
                    visited[mx][my] = True
                    myQueue.append([mx, my])
        if flag == True:
            break
        distance += 1
    distance -= 1
    
    if flag == False:
        distance = 0
    print("#{0} {1}".format(test_case+1, distance))

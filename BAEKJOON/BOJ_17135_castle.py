# 3 <= N, M <= 15
# 1 <= D <= 10
import collections

dx = [0, -1, 0]
dy = [-1, 0, 1]

def castle_tracking(idx):
    global arrange_list
    global N, M, D, result
    global map_list

    if idx >= 2:
        if arrange_list[idx-2] >= arrange_list[idx-1]:
            return None

    if idx >= 3:
        temp_result = 0
        temp_list =[]
        for i in range(N):
            row_list = []
            for j in range(M):
                row_list.append(map_list[i][j])
            temp_list.append(row_list)

        while True:
            die_list = []
            for i in range(3):
                visited = [[False for i in range(M)] for j in range(N)]

                myQueue = collections.deque([])
                visited[N-1][arrange_list[i]] = True
                myQueue.append([N-1, arrange_list[i]])
                while myQueue:
                    current = myQueue.popleft()
                    if temp_list[current[0]][current[1]] == 1:
                        if [current[0], current[1]] not in die_list:
                            die_list.append([current[0], current[1]])
                        break
                    
                    for j in range(3):
                        mx = current[0] + dx[j]
                        my = current[1] + dy[j]
                        if mx < 0 or my < 0 or my >= M:
                            continue
                        if visited[mx][my] == False and (abs(mx-N)+abs(my-arrange_list[i])) <= D:
                            visited[mx][my] = True
                            myQueue.append([mx, my])
            for i in die_list:
                temp_list[i[0]][i[1]] = 0
                temp_result += 1

            flag = True
            for i in range(N):
                for j in range(M):
                    if temp_list[i][j] == 1:
                        flag = False
                        break
                if flag == False:
                    break
            if flag == True:
                if result < temp_result:
                    result = temp_result
                return None
            
            for i in range(N):
                for j in range(M):
                    if i != N-1:
                        temp_list[N-1-i][j] = temp_list[N-1-i-1][j]
                    else:
                        temp_list[N-1-i][j] = 0
    else:
        for i in range(M):
            arrange_list[idx] = i
            castle_tracking(idx+1)

N, M, D = map(int, input().split())
map_list = []
for i in range(N):
    row_list = list(map(int, input().split()))
    map_list.append(row_list)

result = 0
arrange_list = [0 for i in range(3)]
castle_tracking(0)
print("{0}".format(result))
# 흑 : 1, 백 : 2
t = int(input())
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(t):
    NM_list = list(map(int, input().split(" ")))
    N = NM_list[0]
    M = NM_list[1]
    result_W = 0
    result_B = 0
    int_N2 = int(N/2)

    pro_MAP = [[0 for x in range(N)] for y in range(N)]

    pro_MAP[int_N2-1][int_N2-1] = 2
    pro_MAP[int_N2][int_N2] = 2
    pro_MAP[int_N2-1][int_N2] = 1
    pro_MAP[int_N2][int_N2-1] = 1

    for j in range(M):
        xywb_list = list(map(int, input().split(" ")))
        x = xywb_list[0] - 1
        y = xywb_list[1] - 1
        wb = xywb_list[2]

        pro_MAP[y][x] = wb

        origin_x = x
        origin_y = y

        for k in range(8):
            flag = True
            cnt = 0
            mx = origin_x
            my = origin_y
            x = origin_x
            y = origin_y

            if y+dx[k]<0 or y+dx[k]>=N or x+dy[k]<0 or x+dy[k]>=N or pro_MAP[y+dx[k]][x+dy[k]] == 0:
                continue

            while pro_MAP[my+dx[k]][mx+dy[k]] == (wb%2+1):
                my += dx[k]
                mx += dy[k]
                cnt += 1
                if my+dx[k]<0 or my+dx[k]>=N or mx+dy[k]<0 or mx+dy[k]>=N or pro_MAP[my+dx[k]][mx+dy[k]] == 0:
                    flag = False
                    break
            
            if flag == True:
                for l in range(cnt):
                    pro_MAP[y+dx[k]][x+dy[k]] = wb
                    y += dx[k]
                    x += dy[k]

    for j in range(N):
        for k in range(N):
            if pro_MAP[j][k] == 1:
                result_W += 1
            elif pro_MAP[j][k] == 2:
                result_B += 1
    
    print("#{0} {1} {2}".format(i+1, result_W, result_B))
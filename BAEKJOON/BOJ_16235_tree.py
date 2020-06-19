CONST_INT_NMAX = 12

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

result = 0

nmk_list = list(map(int, input().split()))
n = nmk_list[0]
m = nmk_list[1]
k = nmk_list[2]

plus_map = [[0 for y in range(CONST_INT_NMAX)] for x in range(CONST_INT_NMAX)]
enage_map = [[[] for y in range(CONST_INT_NMAX)] for x in range(CONST_INT_NMAX)]

for i in range(n):
    plus_list = list(map(int, input().split()))
    for j in range(n):
        plus_map[i][j] = plus_list[j]
        enage_map[i][j].append(5)
        enage_map[i][j].append([])

for i in range(m):
    xyage_list = list(map(int, input().split()))
    x = xyage_list[0]
    y = xyage_list[1]
    age = xyage_list[2]
    enage_map[x-1][y-1][1].append(age)

for i in range(k):
    # 봄, 여름
    for j in range(n):
        for k in range(n):

            enage_map[j][k][1].sort()
            temp_list = []
            temp_sum = 0

            for l in enage_map[j][k][1]:
                if l > enage_map[j][k][0]:
                    temp_sum += int(l/2)
                else:
                    temp_list.append(l+1)
                    enage_map[j][k][0] -= l
            
            enage_map[j][k][0] += temp_sum
            enage_map[j][k][1] = temp_list
    
    # 가을
    for j in range(n):
        for k in range(n):
            for l in enage_map[j][k][1]:
                if l%5 == 0:
                    for m in range(8):
                        if j+dx[m]<0 or j+dx[m]>=n or k+dy[m]<0 or k+dy[m]>=n:
                            continue
                        mx = j + dx[m]
                        my = k + dy[m]
                        enage_map[mx][my][1].append(1)

    # 겨울
    for j in range(n):
        for k in range(n):
            enage_map[j][k][0] += plus_map[j][k]

for j in range(n):
    for k in range(n):
        result += len(enage_map[j][k][1])

print(result)
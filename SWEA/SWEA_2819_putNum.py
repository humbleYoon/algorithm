dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())

checked = [0 for i in range(10000000)]

for test_case in range(T):
    map_info = []
    for i in range(4):
        temp_list = list(map(int, input().split()))
        map_info.append(temp_list)
    Table = [[] for i in range(7)]
    for i in range(7):
        if i == 0:
            for j in range(4):
                for k in range(4):
                    Table[i].append([map_info[j][k], j, k])
        else:
            for j in Table[i-1]:
                for k in range(4):
                    if j[1] + dx[k] < 0 or j[1] + dx[k] > 3 or j[2] + dy[k] < 0 or j[2] + dy[k] > 3:
                        continue
                    Table[i].append([j[0]*10+map_info[j[1]+dx[k]][j[2]+dy[k]], j[1]+dx[k], j[2]+dy[k]])
    result = 0
    for i in Table[6]:
        if checked[i[0]] == 0:
            checked[i[0]] = 1
            result += 1
    print("#{0} {1}".format(test_case+1, result))

    for i in Table[6]:
        checked[i[0]] = 0
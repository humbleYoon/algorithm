T = int(input())
for test_case in range(T):
    N, M, C = map(int, input().split())
    map_info = []
    for i in range(N):
        map_info.append(list(map(int, input().split())))
    result = 0
    for i in range(N):
        for j in range(N):
            if j + (M-1) >= N:
                continue
            max_honey1 = 0
            Table1 = [[] for k in range(M)]
            for k in range(M):
                if k == 0:
                    Table1[k].append([map_info[i][j+k]**2, C-map_info[i][j+k]])
                    if map_info[i][j+k]**2 > max_honey1:
                        max_honey1 = map_info[i][j+k]**2
                    Table1[k].append([0, C])
                else:
                    for l in range(0, k):
                        for m in Table1[l]:
                            if m[1]-map_info[i][j+k] >= 0:
                                Table1[k].append([m[0]+map_info[i][j+k]**2, m[1]-map_info[i][j+k]])
                                if m[0]+map_info[i][j+k]**2 > max_honey1:
                                    max_honey1 = m[0]+map_info[i][j+k]**2
            for k in range(i, N):
                for l in range(0, N):
                    if k == i:
                        if l < j+M:
                            continue
                    if l + (M-1) >= N:
                        continue
                    max_honey2 = 0
                    Table2 = [[] for m in range(M)]
                    for m in range(M):
                        if m == 0:
                            Table2[m].append([map_info[k][l+m]**2, C-map_info[k][l+m]])
                            if map_info[k][l+m]**2 > max_honey2:
                                max_honey2 = map_info[k][l+m]**2
                            Table2[m].append([0, C])
                        else:
                            for n in range(0, m):
                                for o in Table2[n]:
                                    if o[1]-map_info[k][l+m] >= 0:
                                        Table2[m].append([o[0]+map_info[k][l+m]**2, o[1]-map_info[k][l+m]])
                                        if o[0]+map_info[k][l+m]**2 > max_honey2:
                                            max_honey2 = o[0]+map_info[k][l+m]**2
                    if max_honey1 + max_honey2 > result:
                        result = max_honey1 + max_honey2
    print("#{0} {1}".format(test_case+1, result))

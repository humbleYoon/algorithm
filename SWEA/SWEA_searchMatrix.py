CONST_INT_MAX = 105

T = int(input())

for test_case in range(T):
    n = int(input())
    map_list = []
    visited = [[False for i in range(CONST_INT_MAX)] for j in range(CONST_INT_MAX)]
    result = []
    for i in range(n):
        row_list = list(map(int, input().split()))
        map_list.append(row_list)
    for i in range(n):
        for j in range(n):
            if map_list[i][j] != 0 and visited[i][j] == False:
                mx = i
                my = j
                while my < n:
                    if map_list[i][my] != 0 and visited[i][my] == False:
                        my += 1
                    else:
                        break
                distanceY = my - j
                while mx < n:
                    if map_list[mx][j] != 0 and visited[mx][j] == False:
                        mx += 1
                    else:
                        break
                distanceX = mx - i
                for k in range(i, mx):
                    for l in range(j, my):
                        visited[k][l] = True
                result.append([distanceX, distanceY])
    for i in range(len(result)-1):
        for j in range(len(result)-1-i):
            if result[j][0]*result[j][1] > result[j+1][0]*result[j+1][1]:
                result[j][0], result[j][1], result[j+1][0], result[j+1][1] = result[j+1][0], result[j+1][1], result[j][0], result[j][1]
            elif result[j][0]*result[j][1] == result[j+1][0]*result[j+1][1]:
                if result[j][0] > result[j][1]:
                    result[j][0], result[j][1], result[j+1][0], result[j+1][1] = result[j+1][0], result[j+1][1], result[j][0], result[j][1]

    print("#{0} {1} ".format(test_case+1, len(result)), end='')
    for i in result:
        print("{0} {1} ".format(i[0], i[1]), end='')
    print()
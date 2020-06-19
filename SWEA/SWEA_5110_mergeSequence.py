T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    info_list = []
    for i in range(M):
        temp_list = list(map(int, input().split()))
        row_list = []
        if i == 0:
            for j in range(N):
                if j == 0:
                    row_list.append([i, -1, temp_list[j], i, 1]) # 0, -1을 가리키는 것이 시작 노드
                elif j == N-1:
                    row_list.append([i, j-1, temp_list[j], i, N]) # 0, N을 가리키는 것이 끝 노드
                else:
                    row_list.append([i, j-1, temp_list[j], i, j+1])
            info_list.append(row_list)
            start_x = 0
            start_y = 0
        else:
            # 링크드 리스트를 따라가면서 들어오는 수열의 첫 숫자보다 높은 값(인덱스)을 찾는다
            # 그 인덱스가 맨 앞의 경우, 시작노드를 들어오는 수열의 첫 숫자로 바꿔주고, 끝 숫자가 원래 있던 수열의 첫 노드를 가리키도록 한다
            # 중간에 있을 경우, 찾은 노드의 앞 노드가 들어오는 수열의 첫 숫자를 가리키도록, 들어오는 수열의 끝 숫자가 찾은 노드를 가리키도록 한다
            # 끝에 있을 경우, 끝 노드가 들어오는 수열의 첫 숫자를 가리키도록, 들어오는 수열의 끝 숫자가 끝 노드가 된다
            # 이 때, 들어오는 수열들 사이사이를 이어주는 것도 빼먹지 말아야 한다
            for j in range(N):
                if j == 0:
                    mx = start_x
                    my = start_y
                    flag = True
                    flag2 = -1
                    while mx != 0 or my != N:
                        if temp_list[0] >= info_list[mx][my][2]:
                            end_x = mx
                            end_y = my
                            mx, my = info_list[mx][my][3], info_list[mx][my][4]
                        else:
                            flag = False
                            break
                    if flag == False:
                        if info_list[mx][my][0] == 0 and info_list[mx][my][1] == -1:
                            # 첫 노드를 가리키는 애가 들어오는 수열의 첫 숫자보다 클 때
                            row_list.append([0, -1, temp_list[j], i, j+1])
                            info_list[start_x][start_y][0] = i
                            info_list[start_x][start_y][1] = N-1
                            start_x = i
                            start_y = 0
                            flag2 = 0
                        else:
                            # 들어오는 수열이 중간에 들어갈 때
                            pre_x = info_list[mx][my][0]
                            pre_y = info_list[mx][my][1]
                            row_list.append([pre_x, pre_y, temp_list[j], i, j+1])
                            info_list[pre_x][pre_y][3] = i
                            info_list[pre_x][pre_y][4] = j
                            info_list[mx][my][0] = i
                            info_list[mx][my][1] = N-1
                            flag2 = 1
                    else:
                        # 끝에 들어갈 경우
                        info_list[end_x][end_y][3] = i
                        info_list[end_x][end_y][4] = j
                        row_list.append([end_x, end_y, temp_list[j], i, j+1])
                        flag2 = 2
                elif j == N-1:
                    if flag2 == 0 or flag2 == 1:
                        row_list.append([i, j-1, temp_list[j], mx, my])
                    else:
                        row_list.append([i, j-1, temp_list[j], 0, N])
                else:
                    row_list.append([i, j-1, temp_list[j], i, j+1])
            info_list.append(row_list)
    
    print("#{0} ".format(test_case+1), end='')
    mx = start_x
    my = start_y
    while info_list[mx][my][3] != 0 or info_list[mx][my][4] != N:
        mx, my = info_list[mx][my][3], info_list[mx][my][4]
    for i in range(10):
        print("{0} ".format(info_list[mx][my][2]), end='')
        mx, my = info_list[mx][my][0], info_list[mx][my][1]
    print()
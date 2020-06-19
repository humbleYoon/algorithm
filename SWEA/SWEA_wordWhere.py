T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    info_list = []
    result = 0
    for i in range(N):
        row_list = list(map(int, input().split()))
        info_list.append(row_list)
    for i in range(N):
        for j in range(N):
            if info_list[i][j] == 1:
                idx = j+1
                length = 1
                if j-1 == -1:
                    while idx < N and info_list[i][idx] == 1:
                        idx += 1
                        length += 1
                else:
                    if info_list[i][j-1] == 0:
                        while idx < N and info_list[i][idx] == 1:
                            idx += 1
                            length += 1
                if length == K:
                    result += 1

                idx = i+1
                length = 1
                if i-1 == -1:
                    while idx < N and info_list[idx][j] == 1:
                        idx += 1
                        length += 1
                else:
                    if info_list[i-1][j] == 0:
                        while idx < N and info_list[idx][j] == 1:
                            idx += 1
                            length += 1
                if length == K:
                    result += 1
    print("#{0} {1}".format(test_case+1, result))
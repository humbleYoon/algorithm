# 1. 0이 사이에 채워져있는 공백 상태를 없애기 위해 0 자리를 다 땡김
# 2. 하나씩 보면서 같으면? 합쳐주고, 다르면? 무시하고

T = int(input())
for test_case in range(T):
    N, udlr = input().split()
    N = int(N)
    info_list = []
    for i in range(N):
        row_list = list(map(int, input().split()))
        info_list.append(row_list)
    
    if udlr == 'up':
        for i in range(N):
            for j in range(1, N):
                if info_list[j][i] != 0:
                    idx = j-1
                    while idx >= 0:
                        if info_list[idx][i] != 0:
                            break
                        idx -= 1
                    info_list[idx+1][i], info_list[j][i] = info_list[j][i], info_list[idx+1][i]
        for i in range(N):
            for j in range(N-1):
                if info_list[j][i] == info_list[j+1][i]:
                    info_list[j][i] += info_list[j+1][i]
                    for k in range(N-1-(j+1)):
                        info_list[j+1+k][i] = info_list[j+1+k+1][i]
                    info_list[N-1][i] = 0
    elif udlr == 'down':
        for i in range(N):
            for j in range(N-2, -1, -1):
                if info_list[j][i] != 0:
                    idx = j+1
                    while idx <= N-1:
                        if info_list[idx][i] != 0:
                            break
                        idx += 1
                    info_list[idx-1][i], info_list[j][i] = info_list[j][i], info_list[idx-1][i]
        for i in range(N):
            for j in range(N-1):
                if info_list[N-j-1][i] == info_list[N-j-1-1][i]:
                    info_list[N-j-1][i] += info_list[N-j-1-1][i]
                    for k in range(N-1-(j+1)):
                        info_list[N-j-1-1-k][i] = info_list[N-j-1-1-k-1][i]
                    info_list[0][i] = 0
    elif udlr == 'left':
        for i in range(N):
            for j in range(1, N):
                if info_list[i][j] != 0:
                    idx = j-1
                    while idx >= 0:
                        if info_list[i][idx] != 0:
                            break
                        idx -= 1
                    info_list[i][idx+1], info_list[i][j] = info_list[i][j], info_list[i][idx+1]
        for i in range(N):
            for j in range(N-1):
                if info_list[i][j] == info_list[i][j+1]:
                    info_list[i][j] += info_list[i][j+1]
                    for k in range(N-1-(j+1)):
                        info_list[i][j+1+k] = info_list[i][j+1+k+1]
                    info_list[i][N-1] = 0
    else:
        for i in range(N):
            for j in range(N-2, -1, -1):
                if info_list[i][j] != 0:
                    idx = j+1
                    while idx <= N-1:
                        if info_list[i][idx] != 0:
                            break
                        idx += 1
                    info_list[i][idx-1], info_list[i][j] = info_list[i][j], info_list[i][idx-1]
        for i in range(N):
            for j in range(N-1):
                if info_list[i][N-j-1] == info_list[i][N-j-1-1]:
                    info_list[i][N-j-1] += info_list[i][N-j-1-1]
                    for k in range(N-1-(j+1)):
                        info_list[i][N-j-1-1-k] = info_list[i][N-j-1-1-k-1]
                    info_list[i][0] = 0
                        
    print("#{0}".format(test_case+1))
    for i in range(N):
        for j in range(N):
            print("{0} ".format(info_list[i][j]), end='')
        print()
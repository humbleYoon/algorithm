T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = []
    result = ''
    for i in range(N):
        data.append(input())
    
    for i in range(N):
        for j in range(N-M+1):
            f_idx = j
            b_idx = j+M-1
            flag1 = True
            flag2 = True
            while f_idx <= b_idx:
                if data[i][f_idx] != data[i][b_idx]:
                    flag1 = False
                if data[f_idx][i] != data[b_idx][i]:
                    flag2 = False       
                f_idx += 1
                b_idx -= 1

            if flag1 == True:
                for k in range(M):
                    result = result + data[i][j+k]
            if flag2 == True:
                for k in range(M):
                    result = result + data[j+k][i]
    print("#{0} {1}".format(test_case+1, result))

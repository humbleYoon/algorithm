# 90도 회전 첫행, 180도 회전 첫행, 270도 회전 첫행
# 90도 회전 두번째행, 180도 회전 두번째행, 270도 회전 두번째행
# 90도 회전 세번째행, 180도 회전 세번째행, 270도 회전 세번째행
 
T = int(input())
for test_case in range(T):
    N = int(input())
    N_list = []
    for i in range(N):
        row_list = list(map(int, input().split()))
        N_list.append(row_list)
     
    N_list2 = [[0 for i in range(N)] for j in range(N)]
    N_list3 = [[0 for i in range(N)] for j in range(N)]
    N_list4 = [[0 for i in range(N)] for j in range(N)]
 
    for i in range(N):
        for j in range(N):
            N_list2[i][j] = N_list[N-1-j][i]
            N_list3[i][j] = N_list[N-1-i][N-1-j]
            N_list4[i][j] = N_list[j][N-1-i]
 
    print("#{0}".format(test_case+1))
    for i in range(N):
        for j in range(N):
            print("{0}".format(N_list2[i][j]), end='')
        print(" ", end='')
        for j in range(N):
            print("{0}".format(N_list3[i][j]), end='')
        print(" ", end='')
        for j in range(N):
            print("{0}".format(N_list4[i][j]), end='')
        print()
T = int(input())

for test_case in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    result = -1
    for i in range(0, N-1):
        for j in range(i+1, N):
            multi = N_list[i]*N_list[j]
            if multi // 10 == 0:
                continue
            b_num = multi % 10
            multi = multi // 10
            f_num = multi % 10
            flag = True
            while multi > 0:
                if f_num <= b_num:
                    multi = multi // 10
                    f_num, b_num = multi % 10, f_num
                else:
                    flag = False
                    break
            if flag == True:
                if result < N_list[i]*N_list[j]:
                    result = N_list[i]*N_list[j]
    print("#{0} {1}".format(test_case+1, result))
                 
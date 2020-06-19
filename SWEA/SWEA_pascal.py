CONST_INT_MAX = 15

T = int(input())

for test_case in range(T):
    N = int(input())
    N_list = []
    for i in range(N):
        temp_list = []
        if i == 0:
            temp_list.append(1)
        elif i == 1:
            temp_list.append(1)
            temp_list.append(1)
        else:
            temp_list.append(1)
            for j in range(i-1):
                temp_list.append(N_list[i-1][j]+N_list[i-1][j+1])
            temp_list.append(1)
        N_list.append(temp_list)
    print("#{0}".format(test_case+1))
    for i in range(N):
        for j in N_list[i]:
            print("{0} ".format(j), end='')
        print()
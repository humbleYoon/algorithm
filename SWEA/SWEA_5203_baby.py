#  9 9 5 6 5 6 1 1 4 2 2 1
#  5 3 2 9 1 5 2 0 9 2 0 0
#  2 8 7 7 0 2 2 2 5 4 0 3

T = int(input())

for test_case in range(T):
    p_info = [[0 for i in range(10)] for j in range(2)]
    N_list = list(map(int, input().split()))
    result = 0

    for i in range(12):
        p_info[i%2][N_list[i]] += 1
        if p_info[i%2][N_list[i]] >= 3:
            result = i%2+1
            break
        flag2 = False
        for j in range(3):
            if N_list[i] - j >= 0 and N_list[i] - j + 2 <= 9:
                flag = True
                for k in range(3):
                    if p_info[i%2][N_list[i] - j + k] == 0:
                        flag = False
                        break
                if flag == True:
                    result = i%2+1
                    flag2 = True
                    break
        if flag2 == True:
            break
    print("#{0} {1}".format(test_case+1, result))

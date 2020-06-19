for test_case in range(10):
    find_N = int(input())
    data_map = []
    result = 0
    for i in range(8):
        data_map.append(input())
    
    for i in range(8):
        for j in range(8-find_N+1):
            f_idx = j
            b_idx = j+find_N-1
            flag1 = True
            flag2 = True
            while f_idx <= b_idx:
                if data_map[i][f_idx] != data_map[i][b_idx]:
                    flag1 = False
                if data_map[f_idx][i] != data_map[b_idx][i]:
                    flag2 = False
                f_idx += 1
                b_idx -= 1
            if flag1 == True:
                result += 1
            if flag2 == True:
                result += 1
    
    print("#{0} {1}".format(test_case+1, result))
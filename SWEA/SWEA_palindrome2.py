for test_case in range(10):
    T = int(input())
    data_map = []
    result = 0
    for i in range(100):
        data_map.append(input())
    
    for i in range(100):
        for j in range(100):
            for k in range(100-i):
                f_idx = k
                b_idx = k+i
                flag1 = True
                flag2 = True
                while f_idx <= b_idx:
                    if data_map[j][f_idx] != data_map[j][b_idx]:
                        flag1 = False
                    if data_map[f_idx][j] != data_map[b_idx][j]:
                        flag2 = False
                    f_idx += 1
                    b_idx -= 1
                if flag1 == True:
                    if result < i+1:
                        result = i+1
                if flag2 == True:
                    if result < i+1:
                        result = i+1
    
    print("#{0} {1}".format(T, result))
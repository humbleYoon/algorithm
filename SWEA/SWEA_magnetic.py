for test_case in range(10):
    n_length = int(input())
    map_list = []
    for i in range(100):
        row_list = list(map(int, input().split()))
        map_list.append(row_list)

    result = 0
    for j in range(100):
        # 1: N극, 2: S극
        # 윗 부분에 N극, 아랫 부분에 S극
        # 교착상태: N극 아래에 S극이 나올 때
        flag = False
        for i in range(100):
            if map_list[i][j] == 1:
                flag = True
            elif map_list[i][j] == 2:
                if flag == True:
                    result += 1
                    flag = False
    
    print("#{0} {1}".format(test_case+1, result))

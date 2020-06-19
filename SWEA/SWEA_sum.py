CONST_INT_MAX = 100

T = 10

for test_case in range(T):
    test_case_num = int(input())
    result = -98172386333
    rc_list = []
    for i in range(CONST_INT_MAX):
        row_list = list(map(int, input().split()))
        rc_list.append(row_list)
    
    cross_sum = 0
    cross_sum2 = 0
    for i in range(CONST_INT_MAX):
        r_sum = 0
        c_sum = 0

        cross_sum += rc_list[i][i]
        cross_sum2 += rc_list[99-i][i]

        for j in range(CONST_INT_MAX):
            r_sum += rc_list[i][j]
            c_sum += rc_list[j][i]
        
        if r_sum > result:
            result = r_sum
        
        if c_sum > result:
            result = c_sum
    
    if cross_sum > result:
        result = cross_sum

    if cross_sum2 > result:
        result = cross_sum2

    print("#{0} {1}".format(test_case_num, result))
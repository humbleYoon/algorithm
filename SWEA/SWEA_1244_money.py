CONST_INT_MAX = 10

def money_tracking(c1, c2, func_list, check_num):
    global num_idx
    global result
    global change_num
    if check_num >= change_num:
        temp_sum = 0
        temp_idx = num_idx
        temp_pos = 100000 / 10**(6+num_idx)

        while temp_idx < 0:
            temp_sum += func_list[temp_idx]*temp_pos
            temp_pos = int(temp_pos/10)
            temp_idx += 1

        if temp_sum > result:
            result = temp_sum
    else:
        temp = func_list[c1]
        func_list[c1] = func_list[c2]
        func_list[c2] = temp
        for i in range(0, -1*num_idx-2):
            for j in range(1, -1*num_idx-1):
                # 456789 10
                if i < j:
                    money_tracking(-i-1, -j-1, func_list, check_num+1)
                    return_temp = func_list[c1]
                    func_list[c1] = func_list[c2]
                    func_list[c2] = return_temp

T = int(input())
for test_case in range(T):
    num, change_num = map(int, input().split())
    num_list = [0 for i in range(CONST_INT_MAX)]
    num_idx = -1
    result = -989712386
    while num / 10 != 0:
        num_list[num_idx] = num % 10
        num_idx -= 1
        num = int(num/10)

    for i in range(0, -1*num_idx-2):
        for j in range(1, -1*num_idx-1):
            # 456789 10
            if i < j:
                money_tracking(-i-1, -j-1, num_list, 0)

    print("#{0} {1}".format(test_case+1, int(result)))
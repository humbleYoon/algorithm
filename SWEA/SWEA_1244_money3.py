def money_tracking(c1, c2, num_list, check_num, overlap_list):
    global change_num
    global result
    global num_len

    temp = num_list[c1]
    num_list[c1] = num_list[c2]
    num_list[c2] = temp

    temp_result = 0
    pos = 10 ** (num_len-1)
    for i in num_list:
        temp_result += i*pos
        pos = int(pos/10)

    temp_list = [check_num, temp_result]
    if temp_list in overlap_list:
        return None
    else:
        overlap_list.append(temp_list)

    if check_num >= change_num:
        if result < temp_result:
            result = temp_result
    else:
        for i in range(num_len-1):
            for j in range(i, num_len):
                if i < j:
                    money_tracking(i, j, num_list, check_num+1, overlap_list)
                    temp = num_list[i]
                    num_list[i] = num_list[j]
                    num_list[j] = temp

T = int(input())

for test_case in range(T):
    num, change_num = input().split()
    change_num = int(change_num)
    num_list = []
    num_len = 0
    result = -971623213

    overlap_list=[]

    for i in num:
        num_list.append(int(i))
        num_len += 1

    for i in range(num_len-1):
        for j in range(i, num_len):
            if i < j:
                money_tracking(i, j, num_list, 1, overlap_list)
                temp = num_list[i]
                num_list[i] = num_list[j]
                num_list[j] = temp
    print("#{0} {1}".format(test_case+1, result))
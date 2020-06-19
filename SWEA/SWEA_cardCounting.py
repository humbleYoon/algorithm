# S, D, H, C 각 1 ~ 13
# 문자 세개씩 끊고,
# 첫번째 문자 'S', 'D', 'H', 'C' -> 0, 1, 2, 3
# 두번째 -> '0' -> 세번째 문자만 정수로 바꿔서
# 세번째 -> '1' -> 두번째 문자 + 세번째 문자를 정수로 바꿔서

T = int(input())

for test_case in range(T):
    count_list = [[0 for i in range(14)] for j in range(4)]
    input_str = input()
    flag = True

    for i in range(len(input_str)//3):
        if input_str[3*i] == 'S':
            idx = 0
        elif input_str[3*i] == 'D':
            idx = 1
        elif input_str[3*i] == 'H':
            idx = 2
        else:
            idx = 3

        if input_str[3*i+1] == '0':
            if count_list[idx][int(input_str[3*i+2])] != 0:
                flag = False
                break
            else:
                count_list[idx][int(input_str[3*i+2])] += 1
        elif input_str[3*i+1] == '1':
            if count_list[idx][int(input_str[3*i+1]+input_str[3*i+2])] != 0:
                flag = False
                break
            else:
                count_list[idx][int(input_str[3*i+1]+input_str[3*i+2])] += 1

    if flag == True:
        num = [0, 0, 0, 0]
        for i in range(4):
            for j in range(1, 14):
                if count_list[i][j] == 1:
                    num[i] += 1
        print("#{0} {1} {2} {3} {4}".format(test_case+1, 13-num[0], 13-num[1], 13-num[2], 13-num[3]))
    else:
        print("#{0} ERROR".format(test_case+1))

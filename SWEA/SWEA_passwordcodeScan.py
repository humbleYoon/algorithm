# 각 암호코드의 둘레에는 최소 1칸 이상의 빈 공간이 존재한다
binary_trans = {
    '0': '0000', '1': '0001', '2': '0010','3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

code_trans = {
    211: 0, 221: 1, 122: 2, 411: 3, 132: 4,
    231: 5, 114: 6, 312: 7, 213: 8, 112: 9
}

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    str_list = []
    for i in range(N):
        input_str = input().strip()
        temp_str = ''
        for j in input_str:
            temp_str += binary_trans[j]
        str_list.append(temp_str)
    
    result = 0
    for i in range(1, N):
        idx = M*4-1
        while idx > 54:
            if str_list[i][idx] == '1' and str_list[i-1][idx] == '0':
                num_list = [0, 0, 0, 0, 0, 0, 0, 0]
                for j in range(8):
                    x_list = [0, 0, 0, 0]

                    cnt = 1
                    while idx-1 >= 0 and str_list[i][idx-1] == str_list[i][idx]:
                        idx -= 1
                        cnt += 1
                    x_list[3] = cnt
                    idx -= 1

                    cnt = 1
                    while idx-1 >= 0 and str_list[i][idx-1] == str_list[i][idx]:
                        idx -= 1
                        cnt += 1
                    x_list[2] = cnt
                    idx -= 1
                
                    cnt = 1
                    while idx-1 >= 0 and str_list[i][idx-1] == str_list[i][idx]:
                        idx -= 1
                        cnt += 1
                    x_list[1] = cnt
                    idx -= 1

                    cnt = 1
                    while idx-1 >= 0 and str_list[i][idx-1] == str_list[i][idx]:
                        idx -= 1
                        cnt += 1
                    x_list[0] = cnt
                    idx -= 1

                    x_min = min(x_list)
                    for k in range(4):
                        x_list[k] //= x_min
                    num = x_list[1]*100 + x_list[2]*10 + x_list[3]
                    num_list[7-j] = code_trans[num]
                if ((num_list[0] + num_list[2] + num_list[4] + num_list[6])*3 + num_list[1] + num_list[3] + num_list[5] + num_list[7]) % 10 == 0:
                    result += (num_list[0] + num_list[1] + num_list[2] + num_list[3] + num_list[4] + num_list[5] + num_list[6] + num_list[7])
            else:
                idx -= 1
    print("#{0} {1}".format(test_case+1, result))
        
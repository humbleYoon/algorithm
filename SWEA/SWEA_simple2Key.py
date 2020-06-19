CODE_LENGTH = 56

answer = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2], [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]

T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())
    for i in range(N):
        input_str = input()
        if '1' in input_str:
            inspect_str = input_str
    
    result = 0
    for i in range(M-CODE_LENGTH+1):
        num_list = []
        idx = i-1
        while idx < i+55:
            temp_list = []
            for j in range(7):
                idx += 1
                if j == 0:
                    cnt = 1
                else:
                    if inspect_str[idx-1] == inspect_str[idx]:
                        cnt += 1
                    else:
                        temp_list.append(cnt)
                        cnt = 1
            temp_list.append(cnt)
            if len(temp_list) == 4:
                for j in range(10):
                    if temp_list[0] == answer[j][0] and temp_list[1] == answer[j][1] and temp_list[2] == answer[j][2] and temp_list[3] == answer[j][3]:
                        num_list.append(j)
                        break
        if len(num_list) == 8:
            calculation = 0
            for j in range(4):
                calculation += num_list[j*2]
            calculation *= 3
            for j in range(4):
                calculation += num_list[j*2+1]
            if calculation % 10 == 0:
                for j in range(8):
                    result += num_list[j]
            break
    print("#{0} {1}".format(test_case+1, result))
T = int(input())
for test_case in range(T):
    N, M, L = map(int, input().split())
    N_list = list(map(int, input().split()))
    for i in range(M):
        input_list = list(input().split())
        if input_list[0] == 'I':
            input_list[1] = int(input_list[1])
            input_list[2] = int(input_list[2])
            N_list.insert(input_list[1], input_list[2])
        elif input_list[0] == 'D':
            input_list[1] = int(input_list[1])
            N_list.pop(input_list[1])
        else:
            input_list[1] = int(input_list[1])
            input_list[2] = int(input_list[2])
            N_list[input_list[1]] = input_list[2]
    if L < len(N_list):
        print("#{0} {1}".format(test_case+1, N_list[L]))
    else:
        print("#{0} -1".format(test_case+1))
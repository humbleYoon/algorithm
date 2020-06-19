def metalrod(idx, metalrod_list, pair_n_list):
    global test_case
    global n

    if idx >= 2:
        if metalrod_list[idx-2][1] != metalrod_list[idx-1][0]:
            return None
    
    if idx == n:
        print("#{0} ".format(test_case+1), end='')
        for i in range(n):
            print("{0} {1} ".format(metalrod_list[i][0], metalrod_list[i][1]), end='')
    else:
        for i in range(n):
            metalrod_list[idx] = pair_n_list[i]
            metalrod(idx+1, metalrod_list, pair_n_list)

T = int(input())
for test_case in range(T):
    n = int(input())
    n_list = list(map(int, input().split()))
    pair_n_list = []

    for i in range(n):
        temp_list = []
        temp_list.append(n_list[i*2])
        temp_list.append(n_list[i*2+1])
        pair_n_list.append(temp_list)
    
    metalrod_list = [0 for i in range(n)]
    metalrod(0, metalrod_list, pair_n_list)
    print()
    
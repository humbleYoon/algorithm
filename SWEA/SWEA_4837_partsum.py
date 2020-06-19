T = int(input())

for test_case in range(T):
    result = 0
    N, K = map(int, input().split())
    N_list = []
    for i in range(12):
        N_list.append(i+1)

    for i in range(1<<12):
        temp_list = []
        temp_sum = 0
        for j in range(12):
            if i&(1<<j):
                temp_list.append(N_list[j])

        for j in temp_list:
            temp_sum += j
        
        if temp_sum == K and len(temp_list) == N:
            result += 1
    
    print("#{0} {1}".format(test_case+1, result))
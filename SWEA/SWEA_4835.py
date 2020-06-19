T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))

    sum_max = -912741724
    sum_min = 999999999
    for i in range(N - M + 1):
        temp_sum = 0

        for j in range(M):
            temp_sum += N_list[i+j]

        if temp_sum > sum_max:
            sum_max = temp_sum

        if temp_sum < sum_min:
            sum_min = temp_sum

    print("#{0} {1}".format(test_case+1, sum_max-sum_min))
T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    map_list = []
    result = -9796123631
    for i in range(N):
        row_list = list(map(int, input().split()))
        map_list.append(row_list)
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp_sum = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    temp_sum += map_list[k][l]
            if temp_sum > result:
                result = temp_sum
    print("#{0} {1}".format(test_case+1, result))
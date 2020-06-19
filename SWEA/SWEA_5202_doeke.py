# 끝나는 시간 기준으로 1부터 쭉 감. 가능한 애 있으면 계속 넣음

T = int(input())
for test_case in range(T):
    N = int(input())
    N_list = []
    result = 0
    for i in range(N):
        temp_N = list(map(int, input().split()))
        N_list.append(temp_N)
    s_pivot = 0
    for i in range(1, 25):
        for j in range(N):
            if i == N_list[j][1]:
                if N_list[j][0] >= s_pivot:
                    result += 1
                    s_pivot = i
                    break
    print("#{0} {1}".format(test_case+1, result))

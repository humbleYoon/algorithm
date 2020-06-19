# 해당 화물보다 크거나 같은 컨테이너 중 가장 큰 값의 visited를 체크한다.
# 단, 무게가 큰 애부터 봐야함

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))
    used = [False for i in range(M)]
    result = 0
    N_list.sort()
    for i in range(N):
        n = N_list[N-1-i]
        nm_max = -9871263
        nm_max_idx = -1
        for j in range(M):
            if n <= M_list[j] and used[j] == False:
                if M_list[j] > nm_max:
                    nm_max = M_list[j]
                    nm_max_idx = j
        if nm_max_idx != -1:
            used[nm_max_idx] = True
            result += n
    print("#{0} {1}".format(test_case+1, result))

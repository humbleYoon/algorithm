T = int(input())
for test_case in range(T):
    N, M, L = map(int, input().split())
    N_list = list(map(int, input().split()))
    for i in range(M):
        idx, num = map(int, input().split())
        N_list.insert(idx, num)
    print("#{0} {1}".format(test_case+1, N_list[L]))
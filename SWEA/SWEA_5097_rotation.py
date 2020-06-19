T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    for i in range(M):
        front = N_list.pop(0)
        N_list.append(front)
    print("#{0} {1}".format(test_case+1, N_list[0]))
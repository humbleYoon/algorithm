T = int(input())
for test_case in range(T):
    N, M, K = map(int, input().split())
    N_list = list(map(int, input().split()))
    idx = 0
    for i in range(K):
        idx = (idx + M) % N
        if 0 < idx < N:
            f = N_list[idx-1]
            b = N_list[idx]
            N_list.insert(idx, f+b)
        else:
            f = N_list[N-1]
            b = N_list[0]
            N_list.insert(N, f+b)
            idx -= 1
        N += 1
    print("#{0} ".format(test_case+1), end='')
    for i in range(10):
        if len(N_list) - i > 0:
            print("{0} ".format(N_list[-i-1]), end='')
    print()

    # 958 386 329 169 778
    # 958 386 329 498 169 778 1736 k=2
    # 958 386 715 329 498 169 778 1736 k=3
    # 958 386 715 329 498 667 169 778 1736 k=4
    # 958 386 715 329 498 667 169 778 2514 1736 k=5
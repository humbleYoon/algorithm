T = int(input())
for test_case in range(T):
    N, M, L = map(int, input().split())
    if N%2 == 0:
        graph_info = [0 for i in range(N+2)]
    else:
        graph_info = [0 for i in range(N+1)]
    for i in range(M):
        node, num = map(int, input().split())
        graph_info[node] = num
    if N%2 == 0:
        idx = N
    else:
        idx = N-1
    while True:
        graph_info[idx//2] = graph_info[idx] + graph_info[idx+1]
        if idx//2 == 1:
            break
        idx -= 2
    print("#{0} {1}".format(test_case+1, graph_info[L]))

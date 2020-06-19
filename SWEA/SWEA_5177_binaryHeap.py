T = int(input())
for test_case in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    graph_info = [0]
    graph_idx = 0
    for i in range(N):
        graph_info.append(N_list[i])
        graph_idx += 1
        temp_idx = graph_idx
        while temp_idx//2 >= 1:
            if graph_info[temp_idx] <= graph_info[temp_idx//2]:
                graph_info[temp_idx], graph_info[temp_idx//2] = graph_info[temp_idx//2], graph_info[temp_idx]
                temp_idx //= 2
            else:
                break
    result = 0
    while graph_idx//2 >= 1:
        result += graph_info[graph_idx//2]
        graph_idx //= 2
    print("#{0} {1}".format(test_case+1, result))
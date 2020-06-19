T = 10
def inorder(node):
    global graph_info

    if graph_info[node][1] != 0:
        inorder(graph_info[node][1])
    print("{0}".format(graph_info[node][0]), end='')
    if graph_info[node][2] != 0:
        inorder(graph_info[node][2])

for test_case in range(T):
    N = int(input())
    graph_info = [['', 0, 0] for i in range(N+1)]
    for i in range(N):
        temp_list = list(input().split())
        graph_info[int(temp_list[0])][0] += temp_list[1]
        if len(temp_list) == 3:
            graph_info[int(temp_list[0])][1] = int(temp_list[2])
        elif len(temp_list) == 4:
            graph_info[int(temp_list[0])][1] = int(temp_list[2])
            graph_info[int(temp_list[0])][2] = int(temp_list[3])
    print("#{0} ".format(test_case+1), end='')
    inorder(1)
    print()
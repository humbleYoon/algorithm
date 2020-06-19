T = int(input())

def count_subtree(node):
    global result

    result += 1
    for i in range(2):
        if graph_info[node][i] != 0:
            count_subtree(graph_info[node][i])

for test_case in range(T):
    E, N = map(int, input().split())
    E_list = list(map(int, input().split()))
    graph_info = [[0, 0] for i in range(E+2)]
    for i in range(len(E_list)//2):
        if graph_info[E_list[2*i]][0] == 0:
            graph_info[E_list[2*i]][0] = E_list[2*i+1]
        elif graph_info[E_list[2*i]][1] == 0:
            graph_info[E_list[2*i]][1] = E_list[2*i+1]
    result = 0
    count_subtree(N)
    print("#{0} {1}".format(test_case+1, result))
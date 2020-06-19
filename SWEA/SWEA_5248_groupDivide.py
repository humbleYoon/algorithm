T = int(input())

def group_DFS(node):
    global N, M
    global checked, connected_info

    checked[node] = True
    for i in connected_info[node]:
        if checked[i] == False:
            group_DFS(i)

for test_case in range(T):
    N, M = map(int, input().split())
    checked = [False for i in range(N+1)]
    connected_info = [[] for i in range(N+1)]
    info_list = list(map(int, input().split()))
    for i in range(len(info_list)//2):
        connected_info[info_list[2*i]].append(info_list[2*i+1])
        connected_info[info_list[2*i+1]].append(info_list[2*i])

    result = 0
    for i in range(1, N+1):
        if checked[i] == False:
            result += 1
            group_DFS(i)
    
    print("#{0} {1}".format(test_case+1, result))
T = int(input())

def group_DFS(node):
    global N
    global visited, connected_info

    visited[node] = True
    for i in connected_info[node]:
        if visited[i] == False:
            group_DFS(i)

for test_case in range(T):
    N, M = map(int, input().split())
    connected_info = [[] for i in range(N+1)]
    for i in range(M):
        c1, c2 = map(int, input().split())
        connected_info[c1].append(c2)
        connected_info[c2].append(c1)
    visited = [False for i in range(N+1)]
    result = 0

    for i in range(N):
        if visited[i+1] == False:
            group_DFS(i+1)
            result += 1
    
    print("#{0} {1}".format(test_case+1, result))
        
# 해당 노드에 들어갔을 때 해당 노드에서 이어지는 노드들의 진입 차수를 줄이고,
# 진입 차수가 0이면서 방문하지 않은 곳을 DFS로 다시 들어가는 방식

CONST_INT_MAX = 1050

def orderDfs(current):
    global direction_list
    global entryD_list
    global visited

    visited[current] = True
    print("{0} ".format(current), end='')

    for i in direction_list[current]:
        entryD_list[i] -= 1
    
    for i in direction_list[current]:
        if entryD_list[i] == 0 and visited[i] == False:
            orderDfs(i)

for test_case in range(10):
    direction_list = [[] for i in range(CONST_INT_MAX)]
    entryD_list = [0 for i in range(CONST_INT_MAX)]
    visited = [False for i in range(CONST_INT_MAX)]
    V, E = map(int, input().split())
    E_list = list(map(int, input().split()))
    for i in range(E):
        direction_list[E_list[i*2]].append(E_list[i*2+1])
        entryD_list[E_list[i*2+1]] += 1
    
    print("#{0} ".format(test_case+1))
    for i in range(1, V+1):
        if entryD_list[i] == 0 and visited[i] == False:
            orderDfs(i)
    print()
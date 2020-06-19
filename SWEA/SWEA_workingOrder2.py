# 그래프 방향을 역으로 바꿔주고, 이를 통해 작업 조건을 무시하고 DFS를 한다
# 출력만 역으로 해주면 되므로, 방문체크와 출력문을 DFS 함수의 마지막에 작성한다
# 참고로, 정방향 그래프를 이 방법으로 돌고 출력이 아니라 리스트에 current 노드를 저장한 후 역으로 출력해도 답은 같다
CONST_INT_MAX = 1050

def orderDfs(current):
    global direction_list
    global visited

    for i in direction_list[current]:
        if visited[i] == False:
            orderDfs(i)
    
    visited[current] = True
    print("{0} ".format(current), end='')

for test_case_num in range(10):
    V, E = map(int, input().split())
    E_list = list(map(int, input().split()))
    direction_list = [[] for i in range(CONST_INT_MAX)]
    visited = [False for i in range(CONST_INT_MAX)]
    zeroDegree_list = [False for i in range(CONST_INT_MAX)]
    for i in range(E):
        direction_list[E_list[i*2+1]].append(E_list[i*2])
        zeroDegree_list[E_list[i*2]] = True
    
    print("#{0} ".format(test_case_num+1), end='')
    for i in range(1, V+1):
        if zeroDegree_list[i] == False:
            orderDfs(i)
    print()

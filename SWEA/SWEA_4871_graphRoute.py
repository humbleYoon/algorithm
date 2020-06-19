CONST_INT_MAX = 55

def graphDFS(current):
    global direction_list
    global visited_list
    global endN

    visited_list[current] = True
    
    for i in direction_list[current]:
        if visited_list[i] == False:
            graphDFS(i)

test_case_num = int(input())

for test_case in range(test_case_num):
    V, E = map(int, input().split())
    direction_list = [[] for i in range(CONST_INT_MAX)]
    visited_list = [False for i in range(CONST_INT_MAX)]
    result = 0
    for i in range(E):
        info_fromN, info_toN = map(int, input().split())
        direction_list[info_fromN].append(info_toN)
    startN, endN = map(int, input().split())

    graphDFS(startN)
    if visited_list[endN] == True:
        result = 1
    print("#{0} {1}".format(test_case+1, result))
    
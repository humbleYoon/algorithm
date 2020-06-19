CONST_INT_MAX = 55

T = int(input())
for test_case in range(T):
    myGraph = [[] for i in range(CONST_INT_MAX)]
    visited = [False for i in range(CONST_INT_MAX)]
    myQueue = []
    distance = 0
    result = 0
    V, E = map(int, input().split())
    for i in range(E):
        n1, n2 = map(int, input().split())
        myGraph[n1].append(n2)
        myGraph[n2].append(n1)
    S, G = map(int, input().split())

    visited[S] = True
    myQueue.append(S)
    while myQueue:
        cur_len = len(myQueue)
        for i in range(cur_len):
            current = myQueue.pop(0)
            if current == G:
                result = distance
            for j in myGraph[current]:
                if visited[j] == False:
                    visited[j] = True
                    myQueue.append(j) 
        distance += 1
    
    print("#{0} {1}".format(test_case+1, result))
    
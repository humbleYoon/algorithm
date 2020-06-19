CONST_INT_MAX = 105

T = 10

for test_case in range(T):
    myQueue =[]
    myGraph = [[] for i in range(CONST_INT_MAX)]
    visited = [False for i in range(CONST_INT_MAX)]
    result = 0
    input_length, start = map(int, input().split())
    input_list = list(map(int, input().split()))
    for i in range(input_length//2):
        myGraph[input_list[i*2]].append(input_list[i*2+1])
    
    visited[start] = True
    myQueue.append(start)
    while myQueue:
        cur_length = len(myQueue)
        for i in range(cur_length):
            cur = myQueue.pop(0)
            if i == 0:
                result = cur
            else:
                if result < cur:
                    result = cur
            for j in myGraph[cur]:
                if visited[j] == False:
                    visited[j] = True
                    myQueue.append(j)
    
    print("#{0} {1}".format(test_case+1, result))
    
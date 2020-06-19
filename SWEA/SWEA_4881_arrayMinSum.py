CONST_INT_MAX = 15

def array_tracking(idx, arraySum):
    global N
    global array_list
    global checked
    global result

    if arraySum > result:
        return None
    
    if idx == N:
        if arraySum < result:
            result = arraySum
    else:
        for i in range(N):
            if checked[i] == False:
                checked[i] = True
                array_tracking(idx+1, arraySum+array_list[idx][i])
                checked[i] = False

T = int(input())
for test_case in range(T):
    N = int(input())
    array_list = []
    checked = [False for i in range(CONST_INT_MAX)]
    result = 986873213
    for i in range(N):
        row_list = list(map(int, input().split()))
        array_list.append(row_list)
    
    array_tracking(0, 0)
    print("#{0} {1}".format(test_case+1, result))

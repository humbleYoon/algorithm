T = int(input())

def min_tracking(x, y, temp_sum):
    global N, result, flag
    global map_list

    if temp_sum >= result:
        if flag == True:
            flag = False
        return None

    if flag == True:
        result = temp_sum
        flag = False
    else:
        if x == N-1 and y == N-1:
            flag = True
        if x+1 < N or flag == True:
            min_tracking(x+1, y, temp_sum+map_list[x][y])
        if y+1 < N or flag == True:
            min_tracking(x, y+1, temp_sum+map_list[x][y])
        
for test_case in range(T):
    N = int(input())
    map_list = []
    for i in range(N):
        map_list.append(list(map(int, input().split())))
    result = 9817891239
    flag = False
    min_tracking(0, 0, 0)
    print("#{0} {1}".format(test_case+1, result))
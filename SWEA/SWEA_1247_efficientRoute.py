T = int(input())

def route_tracking(idx, temp_distance, pre_x, pre_y):
    global N, result
    global position_list, checked

    if temp_distance >= result:
        return None
    
    if idx >= N+1:
        result = temp_distance
    elif idx == N:
        route_tracking(idx+1, temp_distance+abs(position_list[2]-pre_x)+abs(position_list[3]-pre_y), position_list[2], position_list[3])
    else:
        for i in range(N):
            if checked[i] == 0:
                checked[i] = 1
                route_tracking(idx+1, temp_distance+abs(position_list[4+2*i]-pre_x)+abs(position_list[4+2*i+1]-pre_y), position_list[4+2*i], position_list[4+2*i+1])
                checked[i] = 0


for test_case in range(T):
    N = int(input())
    position_list = list(map(int, input().split()))
    checked = [0 for i in range(N)]
    result = 9898738974
    route_tracking(0, 0, position_list[0], position_list[1])
    print("#{0} {1}".format(test_case+1, result))
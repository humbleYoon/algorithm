T = int(input())

def threeMonth_tracking(idx, temp_cost):
    global min_info, cost_info
    global result

    if idx >= 12:
        if result > temp_cost:
            result = temp_cost
    else:
        if idx <= 9:
            temp_sum = min_info[idx] + min_info[idx+1] + min_info[idx+2]
        elif idx == 10:
            temp_sum = min_info[idx] + min_info[idx+1]
        else:
            temp_sum = min_info[idx]
        if cost_info[2] < temp_sum:
            threeMonth_tracking(idx+3, temp_cost-(temp_sum-cost_info[2]))
        threeMonth_tracking(idx+1, temp_cost)

for test_case in range(T):
    cost_info = list(map(int, input().split()))
    use_info = list(map(int, input().split()))
    result = sum(use_info)*cost_info[0]
    min_info = [0 for i in range(12)]

    temp_result = 0
    idx = 0
    for i in use_info:
        if i >= cost_info[1]//cost_info[0]:
            temp_result += cost_info[1]
            min_info[idx] = cost_info[1]
        else:
            temp_result += cost_info[0]*i
            min_info[idx] = cost_info[0]*i
        idx += 1
    if temp_result < result:
        result = temp_result
    
    threeMonth_tracking(0, result)
    if result > cost_info[3]:
        result = cost_info[3]
    print("#{0} {1}".format(test_case+1, result))
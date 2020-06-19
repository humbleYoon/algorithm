# 순열
T = int(input())

def battery_tracking(idx, pre, post, temp_sum):
    global N, result
    global cost_info

    if idx > 0:
        temp_sum += cost_info[pre][post]
    if idx >= N-1:
        temp_sum += cost_info[post][0]

    if temp_sum >= result:
        return None

    if idx >= N-1:
        result = temp_sum
    else:
        for i in range(0, N):
            if checked[i] == False:
                checked[i] = True
                battery_tracking(idx+1, post, i, temp_sum)
                checked[i] = False


for test_case in range(T):
    N = int(input())
    cost_info = []
    for i in range(N):
        cost_info.append(list(map(int, input().split())))
    result = 9871946173
    checked = [False for i in range(N)]
    checked[0] = True
    battery_tracking(0, 0, 0, 0)
    print("#{0} {1}".format(test_case+1, result))
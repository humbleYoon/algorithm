# 1번 사람 : 1 ~ N 의 일 중 하나
# 2번 사람 : 1 ~ N 의 일 중 하나(중복 불가)
# 3번 사람 : 1 ~ N 의 일 중 하나
# 순열
# 잘라내기 : 현재 최대 확률값보다 작으면? 절대 커질 수 없으므로 잘라내기 

T = int(input())

def work_tracking(idx, current_percentage):
    global N
    global percentage_list, checked_list
    global result

    if current_percentage <= result:
        return None
    
    if idx == N:
        result = current_percentage
    else:
        for i in range(N):
            if checked_list[i] == False:
                checked_list[i] = True
                work_tracking(idx+1, current_percentage*(percentage_list[idx][i]/100))
                checked_list[i] = False

for test_case in range(T):
    N = int(input())
    percentage_list = []
    for i in range(N):
        temp_list = list(map(int, input().split()))
        percentage_list.append(temp_list)
    
    result = -0.000000001
    checked_list = [False for i in range(N)]
    work_tracking(0, 1)
    print("#{0} {1:0.6f}".format(test_case+1, round(result*100, 6)))
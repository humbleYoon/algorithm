# 백트래킹 -> 1~10명의 사람이 1번, 2번 계단으로 가는 경우를 모두 찾음. 잘라내기 불필요
#         -> 총 2**10 = 1000

# 계단 입구까지 이동 시간을 리스트에 채워넣고 반복문 돌면서 하나씩 감소
# 0이 되는 애부터 계단 큐에 넣음. 동시에 3명 이상 와도 상관 없음 그냥 앞에서부터 넣음. 나머진 대기
# 계단 들어간 애는 이동 시간을 -1로 바꿔줘야 함

# 계단 큐에 들어간 애들은 '자기가 들어간 시간 + 계단 시간 = 나오는 시간'이 되면 큐 나오고, 대기하는 애가 있으면 다시 채워 넣음
# 내려온 애들은 체크 해주고, 반복문 끝에서 모든 애들이 체크 돼 있는지 확인해서 소요 시간 구하고, 그 전의 최솟값과 비교해서 답을 구한다.
import queue

def lunch_tracking(lunch_idx):
    global people_num
    global result
    global stair_selection
    if lunch_idx == people_num:
        distance_list = []
        for i in range(people_num):
            distance = 0
            x_dis = stair_list[stair_selection[i]][0] - people_list[i][0]
            y_dis = stair_list[stair_selection[i]][1] - people_list[i][1]
            if x_dis < 0:
                x_dis *= -1
            if y_dis < 0:
                y_dis *= -1
            distance_list.append(x_dis + y_dis)
        
        stair1 = queue.Queue()
        stair2 = queue.Queue()
        stair_status = [stair1, stair2]

        time_result = 1
        check = [False]*people_num
        while True:
            for i in range(2):
                while stair_status[i].empty() == False:
                        if stair_status[i].queue[0][1] == time_result:
                            check[stair_status[i].queue[0][0]] = True
                            stair_status[i].get()
                        else:
                            break

            for i in range(people_num):
                wait_flag = 0
                if distance_list[i] > 0:
                    distance_list[i] -= 1
                    wait_flag = 1
                if distance_list[i] == 0 and stair_status[stair_selection[i]].qsize() < 3:
                    stair_depth = map_list[stair_list[stair_selection[i]][0]][stair_list[stair_selection[i]][1]]
                    stair_status[stair_selection[i]].put([i, time_result+stair_depth+wait_flag])
                    distance_list[i] -= 1
                
            if False not in check:
                if result > time_result:
                    result = time_result
                break
            
            time_result += 1
        return None
    else:
        for i in range(2):
            stair_selection[lunch_idx] = i
            lunch_tracking(lunch_idx+1)

T = int(input())
for test_case in range(T):
    N = int(input())
    map_list = []
    people_list = []
    stair_list = []
    for i in range(N):
        row_list = list(map(int, input().split()))
        map_list.append(row_list)
    for i in range(N):
        for j in range(N):
            if map_list[i][j] == 1:
                temp_list = [i,j]
                people_list.append(temp_list)
            if map_list[i][j] >= 2:
                temp_list = [i,j]
                stair_list.append(temp_list)

    people_num = len(people_list)
    stair_selection = [0 for i in range(people_num)]
    result = 9781652746
    lunch_tracking(0)
    print("#{0} {1}".format(test_case+1, result))
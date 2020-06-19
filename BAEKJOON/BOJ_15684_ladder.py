# 사다리의 연결 정보를 리스트로 저장
# ex) 1번 줄의 1번 가로줄이 그어져 있다면? [1, 1] = 1
# 그어져 있지 않다면 [1, 1] = 0
# => 필요한 리스트의 크기는 세로줄: 10, 각 세로줄의 가능한 가로줄: 30

# 1. 추가 안하고 다 자기 번호로 가는지 확인
# 가는 과정은 1에서 밑으로 내려오다가 [1, ?] = 1 이면 2로 가고 ? 보다 밑에서 [1, ??](왼쪽)
# 과 [2, ???](오른쪽) 를 확인. 양쪽 다 확인해야하므로.
# 그러다가 제일 밑점에 오면 도착

# 2. 하나 추가 => N*H (300) 의 경우의 수 => 다만, 배열 범위 벗어나는거, 왼쪽 오른쪽 연달아 있지 않도록
# 하는거 주의
# 3. 두개 추가 => 300 C 2 => 45000의 경우의 수(백트래킹) => 주의할 점 마찬가지
# 4. 세개 추가 => 300 C 3 => 4500000의 경우의 수(백트래킹) => 주의할 점 마찬가지
# 5. 각 경우에서 최악의 경우는 세로로 30, 가로로 10 이므로 1350000000이므로 2초 안에 가능
# 6. 조합이 아니라 순열로 하면(*6) 최악의 경우 8억이므로 시간초과

CONST_INT_N_MAX = 12
CONST_INT_H_MAX = 35
ladder_info = [[0 for i in range(CONST_INT_N_MAX)] for j in range(CONST_INT_H_MAX)]
result = -1
flag = False
tracking_list = []

N, M, H = map(int, input().split()) # N: 세로선 개수, M:가로선 개수, H: 세로선마다 놓을 수 있는 가로선 개수

def ladder_tracking(idx, end_idx):
    global ladder_info
    global N
    global H
    global flag
    global tracking_list
    if idx >= end_idx:
        if flag == False:
            flag = check_ladder()
    else:
        for i in range(H):
            for j in range(N-1):
                if idx >= 1:
                    if tracking_list[idx-1][0] > i:
                        continue
                    elif tracking_list[idx-1][0] == i and tracking_list[idx-1][1] >= j:
                        continue
                if ladder_info[i][j] == 1:
                    continue
                if j-1 >= 0:
                    if ladder_info[i][j-1] == 1:
                        continue
                if j+1 < N-1:
                    if ladder_info[i][j+1] == 1:
                        continue
                tracking_list.append([i, j])
                ladder_info[i][j] = 1
                ladder_tracking(idx+1, end_idx)
                ladder_info[i][j] = 0
                del tracking_list[idx]
                
def check_ladder():
    global N
    global H
    global ladder_info

    for i in range(N):
        mv_pos = i
        height = 0
        while height <= H-1:
            temp_flag1 = False
            temp_flag2 = False
            if mv_pos-1 >= 0:
                if ladder_info[height][mv_pos-1] == 1:
                    temp_flag1 = True
            if ladder_info[height][mv_pos] == 1:
                temp_flag2 = True

            if temp_flag1 == True:
                mv_pos -= 1
            elif temp_flag2 == True:
                mv_pos += 1
            height += 1
        if i != mv_pos:
            return False
    return True

for i in range(M):
    x, y = map(int, input().split())
    ladder_info[x-1][y-1] = 1

for i in range(4):
    ladder_tracking(0, i)
    if flag == True:
        result = i
        break
    
print("{0}".format(result))

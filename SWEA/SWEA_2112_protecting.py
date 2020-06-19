# D: 세로(3 <= D <= 13), W: 가로(1 <= W <= 20)
# K(1 <= K <= D): 합격기준 => 단면의 모든 세로방향에 대해서 동일한 특성의 셀들이 K개 이상 연속적으로 있는 경우
# 약품 투입 횟수의 최솟값 => 0 ~ D

# 백트래킹 반복 => 약품 투입 횟수만큼
# 끝나는 조건 만족하면 다음 백트래킹 안돌아도 됨
# 배열에 들어가는 값은 세로값들이고, ...
# => 이 방법으로 하면 A, B에 대한 경우의 수는 넣기 힘듦

# 따라서, 각 줄을 A 약품, B 약품, 안 바꿨을 때의 경우의 수로 나눠서 백트래킹 한다
# 최악의 경우 3 ** 13 = 150만
# 각 경우에서 각 열에서 확인하는 경우의 수 : 13
#            각 행에서 확인하는 경우의 수 : 20
# 최악의 경우는 260
# 잘라내기 : 이미 현재 최소 횟수보다 투입 횟수가 크다면 잘라내기

def protect_tracking(idx, putnum):
    # 안 바꿨을 경우: 0, A 약품: 1, B 약품: 2
    global D
    global W
    global K
    global info_list
    global put_list
    global result
    
    # 잘라내기
    if putnum >= result:
        return None
    
    # 끝 단 도달
    if idx >= D:
        temp_list = []
        for i in range(D):
            row_list = []
            for j in range(W):
                if put_list[i] == 0:
                    row_list.append(info_list[i][j])
                elif put_list[i] == 1:
                    row_list.append(0)
                else:
                    row_list.append(1)
            temp_list.append(row_list)

        result_flag = True
        for i in range(W):
            flag = False
            for j in range(D-K+1):
                flag2 = True
                for k in range(K):
                    if temp_list[j][i] != temp_list[j+k][i]:
                        flag2 = False
                        break
                if flag2 == True:
                    flag = True
                    break
            if flag == False:
                result_flag = False
                break
        if result_flag == True:
            result = putnum
    else:
        for i in range(3):
            put_list[idx] = i
            if i == 1 or i == 2:
                protect_tracking(idx+1, putnum+1)
            else:
                protect_tracking(idx+1, putnum)

T = int(input())
for test_case in range(T):
    D, W, K = map(int, input().split())
    info_list = []
    result = 99887843
    for i in range(D):
        row_list = list(map(int, input().split()))
        info_list.append(row_list)
    
    put_list = [0 for i in range(15)]
    protect_tracking(0, 0)
    print("#{0} {1}".format(test_case+1, result))
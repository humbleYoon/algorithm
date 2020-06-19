# 맵은 20 x 20 = 400
# 각 지점에서 좌우 대각선 20 x 20 = 400
# 각 경우의 수에서 최악의 경우 반복문 100+40번까지 계산해도 160000 x 140 <= 20000000 이므로 완전탐색 가능

# 각 경우의 수에서 체크리스트를 통해 값 중복을 확인하고,
# 값이 중복되거나, 배열 범위 벗어날 경우 다음 경우의 수로 넘어감
# 만약, 다음 경우의 수로 넘어가지 않은 경우에는 그 때 디저트의 개수를 답 변수와 비교한다

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

CONST_INT_N_MAX = 22
CONST_INT_D_MAX = 105

T = int(input())
for test_case in range(T):
    result = -1
    map_list = [[0 for i in range(CONST_INT_N_MAX)] for j in range(CONST_INT_N_MAX)]
    N = int(input())
    for i in range(N):
        row_list = list(map(int, input().split()))
        for j in range(N):
            map_list[i][j] = row_list[j]
    
    for i in range(N):
        for j in range(N): # i, j : 기준 좌표
            for k in range(1, N): # k : 우하(우상) 갈 때 범위
                for l in range(1, N): # l : 좌하(좌상) 갈 때 범위
                    mx = i
                    my = j
                    num = 0
                    d_idx = 0
                    flag = True
                    check = []
                    for m in range(CONST_INT_D_MAX):
                        check.append(False)
                    kl_list = [k, l]

                    for m in range(4):
                        for n in range(kl_list[m%2]):
                            mx = mx + dx[d_idx]
                            my = my + dy[d_idx]
                            if mx < 0 or mx >= N or my < 0 or my >= N:
                                flag = False
                                break
                            if check[map_list[mx][my]] == True:
                                flag = False
                                break
                            check[map_list[mx][my]] = True
                            num += 1

                        if flag == False:
                            break
                        d_idx += 1

                    if flag == True:
                        if result < num:
                            result = num

    print("#{0} {1}".format(test_case+1, result))
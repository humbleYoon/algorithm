import time

# 테케 10개 1초 => 1개당 천만번
# N 최대 20
# 중복 안되고 모든 경우의 수 돌아야 함. 빨리 발견된다고 차이가 최소인건 아니니까
# 부분 집합으로 다 돌고
# 잘라내기 => 부분 집합을 하면서 합을 구하고, 합이 B를 넘으면 판단하고 잘라낸다
# 2**20 => 백만이니까 시간 초과 걸릴 수가 없음

T = int(input())

def height_tracking(idx, temp_sum):
    global N, B, result
    global N_list

    if temp_sum >= B:
        if temp_sum - B < result:
            result = temp_sum - B
        return None

    if idx >= N:
        return None
    else:
        height_tracking(idx+1, temp_sum+N_list[idx])
        height_tracking(idx+1, temp_sum)

for test_case in range(T):
    st = time.time()
    N, B = map(int, input().split())
    N_list = list(map(int, input().split()))
    result = 98987615300000000000

    height_tracking(0, 0)
    print("#{0} {1}".format(test_case+1, result))
    print(time.time() - st)
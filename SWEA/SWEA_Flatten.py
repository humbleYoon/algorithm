# import sys
# sys.stdin = open('input.txt',"r")

T = 10
for test_case in range(T):

    dump = int(input())
    height_list = list(map(int, input().split()))

    for i in range(dump):

        flatten_max = -999999124
        max_idx = -1
        flatten_min = 999999999
        min_idx = -1

        for j in range(100):
            if height_list[j] > flatten_max:
                flatten_max = height_list[j]
                max_idx = j

            if height_list[j] < flatten_min:
                flatten_min = height_list[j]
                min_idx = j

        if flatten_max - flatten_min <= 1:
            break;
        else:
            height_list[max_idx] -= 1
            height_list[min_idx] += 1

    # 마지막에 돌았을 때 min, max가 +1, -1 되고 난 이후에도 min, max는 아닐 수도 있으므로 한번 더 min, max를 체크해야 함
    # 파이썬에서는 max, min 함수 있으므로 변수 선언할 때 max, min으로 하지 않도록 주의
    flatten_max = max(height_list)
    flatten_min = min(height_list)
    result = flatten_max - flatten_min

    print("#{0} {1}".format(test_case + 1, result))
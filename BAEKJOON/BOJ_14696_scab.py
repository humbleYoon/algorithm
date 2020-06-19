# 라운드는 1000
CONST_INT_MAX = 1050

N = int(input())
info_list = [[0 for i in range(4)] for j in range(CONST_INT_MAX)]
info_list2 = [[0 for i in range(4)] for j in range(CONST_INT_MAX)]
for i in range(N):
    input_list = list(map(int, input().split()))
    input_list2 = list(map(int, input().split()))
    for j in range(1, len(input_list)):
        info_list[i][input_list[j]-1] += 1
    for j in range(1, len(input_list2)):
        info_list2[i][input_list2[j]-1] += 1

for i in range(N):
    result = 'D'
    for j in range(4):
        if info_list[i][3-j] > info_list2[i][3-j]:
             result = 'A'
             break
        elif info_list[i][3-j] < info_list2[i][3-j]:
            result = 'B'
            break
    print("{0}".format(result))
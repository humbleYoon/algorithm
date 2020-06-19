CONST_INT_MAX = 105

N = int(input())
idx_list = list(map(int, input().split()))
result = [0 for i in range(CONST_INT_MAX)]
result_len = 1
for i in range(N):
    temp = []
    result_idx = 0
    student_idx = i - idx_list[i]
    for j in range(result_len):
        if j == student_idx:
            temp.append(i+1)
        else:
            temp.append(result[result_idx])
            result_idx += 1
    for j in range(result_len):
        result[j] = temp[j]
    result_len += 1
for i in range(result_len-1):
    print("{0} ".format(result[i]), end='')
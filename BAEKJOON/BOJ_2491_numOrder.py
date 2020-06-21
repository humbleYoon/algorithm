# 1 5 3 6 4 7 1 3 2 9 5
# 1 2
# myArray[idx] = idx를 수열의 끝으로 하는 규칙에 맞는 수열 길이의 최댓값
# 바로 전에 있는 값보다 크거나 같다면? (오름차순일 경우) myArray[idx] = myArray[idx-1] + 1
# 작다면? (오름차순일 경우) myArray[idx] = 1
# 시간복잡도: O(n)
N = int(input())
N_list = list(map(int, input().split()))
result_up_list = [1]
result_down_list = [1]
result = 1
for i in range(1, N):
    if N_list[i-1] <= N_list[i]:
        result_up_list.append(result_up_list[i-1]+1)
        if result < result_up_list[i-1]+1:
            result = result_up_list[i-1]+1
    else:
        result_up_list.append(1)
    
    if N_list[i-1] >= N_list[i]:
        result_down_list.append(result_down_list[i-1]+1)
        if result < result_down_list[i-1]+1:
            result = result_down_list[i-1]+1
    else:
        result_down_list.append(1)

print("{0}".format(result))
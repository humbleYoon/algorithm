N, K = map(int, input().split())
N_list = list(map(int, input().split()))
result = 0
max_result = 0
for i in range(K):
    result += N_list[i]
max_result = result
for i in range(N-K):
    result -= N_list[i]
    result += N_list[i+K]
    if result > max_result:
        max_result = result
print("{0}".format(max_result))
student_info = [[0 for i in range(2)] for j in range(6)]
N, K = map(int, input().split())
result = 0
for i in range(N):
    s, g = map(int, input().split())
    student_info[g-1][s] += 1
for i in range(6):
    for j in range(2):
        result += ((student_info[i][j]+(K-1))//K)
print("{0}".format(result))
# 세로축에서 자른 선: 2, 3
# 가로축에서 자른 선: 4
# 이때의 기준은 (0~2, 0~4), (0~2, 4~10) / (2~3, 0~4), (2~3, 4~10) / (3~8, 0~4), (3~8, 4~10)
# 이때의 넓이는 8, 12, 4, 6, 20, 30
result = -998978163
cutting_list = [[] for i in range(2)]
cutting_list[0].append(0)
cutting_list[1].append(0)
M, N = map(int, input().split()) # M: 가로, N: 세로
cutting_num = int(input())

for i in range(cutting_num):
    idx, num = map(int, input().split())
    cutting_list[idx].append(num) # 0: 세로, 1: 가로

cutting_list[0].sort()
cutting_list[1].sort()

for i in range(len(cutting_list[0])):
    if i < len(cutting_list[0])-1:
        row_distance = cutting_list[0][i+1] - cutting_list[0][i]
    else:
        row_distance = N - cutting_list[0][i]
    for j in range(len(cutting_list[1])):
        if j < len(cutting_list[1])-1:
            column_distance = cutting_list[1][j+1] - cutting_list[1][j]
        else:
            column_distance = M - cutting_list[1][j]
        
        if row_distance*column_distance > result:
            result = row_distance*column_distance

print("{0}".format(result))

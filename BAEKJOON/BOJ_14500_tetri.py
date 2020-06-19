CONST_INT_MAX = 505

NM_list = list(map(int, input().split()))
N = NM_list[0]
M = NM_list[1]
tetri_map = [[0 for j in range(CONST_INT_MAX)] for i in range(CONST_INT_MAX)]
result = -9581824193
for i in range(N):
    line_list = list(map(int, input().split(" ")))
    for j in range(M):
        tetri_map[i][j] = line_list[j]

for i in range(N):
    for j in range(M):
        # 파랭이
        if j+3 < M:
            comp_sum = tetri_map[i][j] + tetri_map[i][j+1] + tetri_map[i][j+2] + tetri_map[i][j+3]
            if comp_sum > result:
                result = comp_sum

        if i+3 < N:
            comp_sum = tetri_map[i][j] + tetri_map[i+1][j] + tetri_map[i+2][j] + tetri_map[i+3][j]
            if comp_sum > result:
                result = comp_sum

        # 노랑이
        if j+1 < M and i+1 < N:
            comp_sum = tetri_map[i][j] + tetri_map[i+1][j] + tetri_map[i][j+1] + tetri_map[i+1][j+1]
            if comp_sum > result:
                result = comp_sum

        # 주황이
        if j+1 < M and i+2 < N:
            comp_sum = tetri_map[i][j] + tetri_map[i+1][j] + tetri_map[i+2][j] + tetri_map[i+2][j+1]
            if comp_sum > result:
                result = comp_sum

        if j+2 < M and i+1 < N:
            comp_sum = tetri_map[i][j] + tetri_map[i+1][j] + tetri_map[i][j+1] + tetri_map[i][j+2]
            if comp_sum > result:
                result = comp_sum
        
        if j+1 < M and i+2 < N:
            comp_sum = tetri_map[i][j] + tetri_map[i][j+1] + tetri_map[i+1][j+1] + tetri_map[i+2][j+1]
            if comp_sum > result:
                result = comp_sum

        if j+2 < M and i+1 < N:
            comp_sum = tetri_map[i][j+2] + tetri_map[i+1][j] + tetri_map[i+1][j+1] + tetri_map[i+1][j+2]
            if comp_sum > result:
                result = comp_sum

        # 주황이 대칭
        if j+1 < M and i+2 < N:
            comp_sum = tetri_map[i+2][j] + tetri_map[i+2][j+1] + tetri_map[i+1][j+1] + tetri_map[i][j+1]
            if comp_sum > result:
                result = comp_sum

        if j+2 < M and i+1 < N:
            comp_sum = tetri_map[i][j] + tetri_map[i+1][j] + tetri_map[i+1][j+1] + tetri_map[i+1][j+2]
            if comp_sum > result:
                result = comp_sum

        if j+1 < M and i+2 < N:
            comp_sum = tetri_map[i][j] + tetri_map[i][j+1] + tetri_map[i+1][j] + tetri_map[i+2][j]
            if comp_sum > result:
                result = comp_sum

        if j+2 < M and i+1 < N:
            comp_sum = tetri_map[i][j] + tetri_map[i][j+1] + tetri_map[i][j+2] + tetri_map[i+1][j+2]
            if comp_sum > result:
                result = comp_sum

        # 초록이
        if j+1 < M and i+2 < N:
            comp_sum = tetri_map[i][j] + tetri_map[i+1][j] + tetri_map[i+1][j+1] + tetri_map[i+2][j+1]
            if comp_sum > result:
                result = comp_sum

        if j+2 < M and i+1 < N:
            comp_sum = tetri_map[i+1][j] + tetri_map[i+1][j+1] + tetri_map[i][j+1] + tetri_map[i][j+2]
            if comp_sum > result:
                result = comp_sum

        if j+1 < M and i+2 < N:
            comp_sum = tetri_map[i][j+1] + tetri_map[i+1][j+1] + tetri_map[i+1][j] + tetri_map[i+2][j]
            if comp_sum > result:
                result = comp_sum

        if j+2 < M and i+1 < N:
            comp_sum = tetri_map[i][j] + tetri_map[i][j+1] + tetri_map[i+1][j+1] + tetri_map[i+1][j+2]
            if comp_sum > result:
                result = comp_sum

        # 분홍이
        if j+2 < M and i+1 < N:
            comp_sum = tetri_map[i][j] + tetri_map[i][j+1] + tetri_map[i][j+2] + tetri_map[i+1][j+1]
            if comp_sum > result:
                result = comp_sum

        if j+1 < M and i+2 < N:
            comp_sum = tetri_map[i+1][j] + tetri_map[i+1][j+1] + tetri_map[i][j+1] + tetri_map[i+2][j+1]
            if comp_sum > result:
                result = comp_sum

        if j+2 < M and i+1 < N:
            comp_sum = tetri_map[i][j+1] + tetri_map[i+1][j] + tetri_map[i+1][j+1] + tetri_map[i+1][j+2]
            if comp_sum > result:
                result = comp_sum

        if j+1 < M and i+2 < N:
            comp_sum = tetri_map[i][j] + tetri_map[i+1][j] + tetri_map[i+2][j] + tetri_map[i+1][j+1]
            if comp_sum > result:
                result = comp_sum

print(result)
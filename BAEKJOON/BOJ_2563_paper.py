CONST_INT_MAX = 105
map_list = [[0 for i in range(CONST_INT_MAX)] for j in range(CONST_INT_MAX)]
result = 0
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            map_list[j][k] = 1
    
for i in range(CONST_INT_MAX):
    for j in range(CONST_INT_MAX):
        if map_list[i][j] == 1:
            result += 1

print("{0}".format(result))
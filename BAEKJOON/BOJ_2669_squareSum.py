CONST_INT_MAX = 105

map_list = [[0 for i in range(CONST_INT_MAX)] for y in range(CONST_INT_MAX)]
result = 0
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            map_list[j][k] = 1
    
for j in range(CONST_INT_MAX):
    for k in range(CONST_INT_MAX):
        if map_list[j][k] == 1:
            result += 1

print("{0}".format(result))
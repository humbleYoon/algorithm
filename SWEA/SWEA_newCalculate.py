CONST_INT_MAX = 400

T = int(input())

map_list = [[0 for i in range(CONST_INT_MAX)] for j in range(CONST_INT_MAX)]

num = 1
for i in range(CONST_INT_MAX):
    for j in range(i+1):
        map_list[i-j][j] = num
        num += 1

for test_case in range(T):
    p, q = map(int, input().split())
    
    for i in range(CONST_INT_MAX):
        for j in range(CONST_INT_MAX):
            if map_list[i][j] == p:
                x1, y1 = i+1, j+1
            if map_list[i][j] == q:
                x2, y2 = i+1, j+1
    print("#{0} {1}".format(test_case+1, map_list[x1+x2-1][y1+y2-1]))
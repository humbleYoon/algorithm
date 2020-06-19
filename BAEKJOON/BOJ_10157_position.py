CONST_INT_MAX = 1050

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited = [[False for i in range(CONST_INT_MAX)] for j in range(CONST_INT_MAX)]
C, R = map(int, input().split())
K = int(input())

x = 1
y = 0
num = 0
d_idx = 0
while num != K and num < R*C:
    mx = x + dx[d_idx]
    my = y + dy[d_idx]
    if mx < 1 or mx > C or my < 1 or my > R or visited[mx][my] == True:
        d_idx = (d_idx+1)%4
        continue
    x = mx
    y = my
    num += 1
    visited[x][y] = True

if K > R*C:
    print("0")
else:
    print("{0} {1}".format(x, y))
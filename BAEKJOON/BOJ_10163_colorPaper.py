map_list = [[0 for i in range(101)] for j in range(101)]
result = [0 for i in range(101)]
N = int(input())
for i in range(N):
    x, y, w, h = map(int, input().split())
    for j in range(x, x+w):
        for k in range(y, y+h):
            map_list[j][k] = i+1
for i in range(101):
    for j in range(101):
        result[map_list[i][j]] += 1
for i in range(1, N+1):
    print("{0}".format(result[i]))
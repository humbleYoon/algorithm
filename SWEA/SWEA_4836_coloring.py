T = int(input())

for test_case in range(T):
    result = 0
    map_list = [[0 for i in range(10)] for j in range(10)]
    N = int(input())
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for j in range(r1, r2+1):
            for k in range(c1, c2+1):
                map_list[j][k] += color

    for i in range(10):
        for j in range(10):
            if map_list[i][j] == 3:
                result += 1

    print("#{0} {1}".format(test_case+1, result))
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

T = int(input())
for test_case in range(T):
    N = int(input())
    map_list = []
    for i in range(N):
        row_list = input()
        map_list.append(row_list)
    start_x = N//2
    start_y = N//2
    result = 0
    result += int(map_list[start_x][start_y])
    for i in range((N-1)//2):
        start_x -= 1
        for j in range(4):
            for k in range(i+1):
                start_x += dx[j]
                start_y += dy[j]
                result += int(map_list[start_x][start_y])
    print("#{0} {1}".format(test_case+1, result))
        
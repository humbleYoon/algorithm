# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#        o     o   o             o        o
CONST_INT_MAX = 105

T = int(input())

for test_case in range(T):
    result = 0
    K, N, M = map(int, input().split())
    station_list = list(map(int, input().split()))
    station_status = [0 for i in range(CONST_INT_MAX)]
    for i in station_list:
        station_status[i] = 1

    current = 0
    while True:
        next_position = -1

        if current + K >= N:
            break;

        for i in range(K):
            current += 1
            if station_status[current] == 1:
                next_position = current

        if next_position == -1:
            result = 0
            break;
        else:
            current = next_position
            result += 1

    print("#{0} {1}".format(test_case+1, result))
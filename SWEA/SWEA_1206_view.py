CONST_INT_CMAX = 1010
CONST_INT_RMAX = 260
apt_map = [[0 for y in range(CONST_INT_CMAX)] for x in range(CONST_INT_RMAX)]

for i in range(10):
    result = 0
    apt_num = int(input())
    apt_list = list(map(int, input().split()))
    for j in range(apt_num):
        for k in range(apt_list[j]):
            apt_map[254-k][j] = 1

    for j in range(255):
        for k in range(2, apt_num-2):
            if apt_map[j][k] == 1:
                if apt_map[j][k-1] == 0 and apt_map[j][k-2] == 0 and apt_map[j][k+1] == 0 and apt_map[j][k+2] == 0:
                    result += 1

    print("#{0} {1}".format(i+1, result))

    for j in range(255):
        for k in range(apt_num):
            apt_map[j][k+2] = 0
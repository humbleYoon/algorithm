T = int(input())

for test_case in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    up_list = []
    down_list = []
    for i in N_list:
        up_list.append(i)
        down_list.append(i)

    for i in range(N):
        for j in range(N-1-i):
            if up_list[j] > up_list[j+1]:
                up_list[j], up_list[j+1] = up_list[j+1], up_list[j]

            if down_list[j] < down_list[j+1]:
                down_list[j], down_list[j+1] = down_list[j+1], down_list[j]
    
    up_idx = 0
    down_idx = 0

    print("#{0} ".format(test_case+1), end='')
    for i in range(5):
        print("{0} ".format(down_list[down_idx]), end='')
        down_idx += 1
        print("{0} ".format(up_list[up_idx]), end='')
        up_idx += 1
    print()
T = int(input())
for test_case in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    max = 0
    min = 1000001

    for i in N_list:
        if max < i:
            max = i

        if min > i:
            min = i

    print("#{0} {1}".format(test_case+1, max-min))
T = int(input())
for test_case in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    checked = [False for i in range(10001)]
    Table = [[] for i in range(N)]
    for i in range(N):
        if i == 0:
            Table[i].append(0) # 안들어가거나
            checked[0] = True
            Table[i].append(N_list[i]) # 들어가거나
            checked[N_list[i]] = True
        else:
            for j in range(0, i):
                for k in Table[j]:
                    if checked[k+N_list[i]] == False:
                        Table[i].append(k+N_list[i])
                        checked[k+N_list[i]] = True
    result = 0
    for i in checked:
        if i == True:
            result += 1
    print("#{0} {1}".format(test_case+1, result))
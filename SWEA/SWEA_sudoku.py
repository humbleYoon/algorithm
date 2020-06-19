t = int(input())
for i in range(t):
    info = []
    result = 1

    for j in range(9):
        input_list = list(map(int, input().split(" ")))
        info.append(input_list)
    
    for j in range(9):
        check = [False, False, False, False, False, False, False, False, False]
        check2 = [False, False, False, False, False, False, False, False, False]
        for k in range(9):
            check[info[j][k]-1] = True
            check2[info[k][j]-1] = True
        if False in check or False in check2:
            result = 0

    for j in range(3):
        for k in range(3):
            check = [False, False, False, False, False, False, False, False, False]
            for l in range(3):
                for m in range(3):
                    check[info[j*3+l][k*3+m]-1] = True
            if False in check:
                result = 0
    
    print("#{0} {1}".format(i+1, result))
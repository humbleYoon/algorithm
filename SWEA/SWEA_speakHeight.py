T = int(input())
for test_case in range(T):
    info_list = []
    result = ''
    for i in range(5):
        row_list = input()
        info_list.append(row_list)
    for i in range(15):
        for j in range(5):
            if i < len(info_list[j]):
                result += info_list[j][i]
    print("#{0} {1}".format(test_case+1, result))
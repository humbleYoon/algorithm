T = int(input())
for test_case in range(T):
    str1 = input()
    str2 = input()
    result = 0
    for i in str1:
        temp_num = 0
        for j in str2:
            if i == j:
                temp_num += 1
        if temp_num > result:
            result = temp_num
    print("#{0} {1}".format(test_case+1, result))
T = int(input())
for i in range(T):
    str1 = input()
    str2 = input()
    result = 0
    for j in range(len(str2)-len(str1)+1):
        flag = True
        idx = j
        for k in range(len(str1)):
            if str1[k] != str2[idx]:
                flag = False
                break
            idx += 1
        if flag == True:
            result = 1
    print("#{0} {1}".format(i+1, result))

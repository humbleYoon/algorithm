T = int(input())
for test_case in range(T):
    num = float(input())
    result = ''
    divide_num = 0.5
    while num > 0:
        if num - divide_num >= 0:
            result += '1'
            num -= divide_num
        else:
            result += '0'
        if len(result) >= 13:
            result = 'overflow'
            break
        divide_num /= 2
    print("#{0} {1}".format(test_case+1, result))
    

T = int(input())

def ternary_tracking(idx, change_num):
    global ternary_num
    global ternary_list
    global ternary_sum_list
    
    if change_num > 1:
        return None

    if idx == len(ternary_num) and change_num != 1:
        return None

    if idx == len(ternary_num):
        num = 0
        pivot = 0
        for i in ternary_list[::-1]:
            num += i * (3**pivot)
            pivot += 1
        ternary_sum_list.append(num)
    else:
        for i in range(3):
            ternary_list[idx] = i
            if ternary_list[idx] == int(ternary_num[idx]):
                ternary_tracking(idx+1, change_num)
            else:
                ternary_tracking(idx+1, change_num+1)

def binary_tracking(idx, change_num):
    global binary_num
    global binary_list
    global binary_sum_list
    
    if change_num > 1:
        return None

    if idx == len(binary_num) and change_num != 1:
        return None

    if idx == len(binary_num):
        num = 0
        pivot = 0
        for i in binary_list[::-1]:
            num += i * (2**pivot)
            pivot += 1
        binary_sum_list.append(num)
    else:
        for i in range(2):
            binary_list[idx] = i
            if binary_list[idx] == int(binary_num[idx]):
                binary_tracking(idx+1, change_num)
            else:
                binary_tracking(idx+1, change_num+1)

for test_case in range(T):
    binary_num = input()
    ternary_num = input()

    binary_list = [0 for i in range(len(binary_num))]
    binary_sum_list = []
    binary_tracking(0, 0)

    ternary_list = [0 for i in range(len(ternary_num))]
    ternary_sum_list = []
    ternary_tracking(0, 0)

    for i in binary_sum_list:
        for j in ternary_sum_list:
            if i == j:
                result = i

    print("#{0} {1}".format(test_case+1, result))
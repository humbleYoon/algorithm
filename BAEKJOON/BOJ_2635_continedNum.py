result = -9898874187
result_list = []

num = int(input())

for i in range(1, num+1):
    temp_list = []
    temp_list.append(num)
    temp_list.append(i)
    temp_num = 2
    f_num = num
    b_num = i
    minus = f_num - b_num

    while minus >= 0:
        temp_list.append(minus)
        f_num = b_num
        b_num = minus
        minus = f_num - b_num
        temp_num += 1

    if temp_num > result:
        result = temp_num
        result_list = temp_list

print("{0}".format(result))
for i in result_list:
    print("{0} ".format(i), end='')

test_case_num = int(input())
for test_case in range(test_case_num):
    stack_list = []
    input_str = input()
    for i in input_str:
        if len(stack_list) == 0:
            stack_list.append(i)
        else:
            top = stack_list[-1]
            if top == i:
                stack_list.pop()
            else:
                stack_list.append(i)
    print("#{0} {1}".format(test_case+1, len(stack_list)))
            
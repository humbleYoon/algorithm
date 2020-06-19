test_case_num = int(input())
for i in range(test_case_num):
    input_str = input()
    stack_list = []
    result = 1
    for j in input_str:
        if j == '(' or j == '{':
            stack_list.append(j)
        elif j == ')':
            if len(stack_list) == 0:
                result = 0
                break
            else:
                if stack_list.pop() == '{':
                    result = 0
                    break
        elif j == '}':
            if len(stack_list) == 0:
                result = 0
                break
            else:
                if stack_list.pop() == '(':
                    result = 0
                    break
    if len(stack_list) != 0:
        result = 0
    print("#{0} {1}".format(i+1, result))
    
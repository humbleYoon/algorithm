T = int(input())

for test_case in range(T):
    input_str = input().split()
    stack_list = []
    flag = False
    for i in input_str:
        if i != '+' and i != '-' and i != '*' and i != '/' and i != '.':
            stack_list.append(int(i))
        elif i == '+' or i == '-' or i == '*' or i == '/':
            if len(stack_list) >= 2:
                s1 = stack_list.pop()
                s2 = stack_list.pop()
            else:
                print("#{0} error".format(test_case+1))
                flag = True
                break

            if i == '+':
                stack_list.append(s2+s1)
            elif i == '-':
                stack_list.append(s2-s1)
            elif i == '*':
                stack_list.append(s2*s1)
            else:
                stack_list.append(s2//s1)
        else:
            if len(stack_list) > 1 or len(stack_list) == 0:
                print("#{0} error".format(test_case+1))
            else:
                print("#{0} {1}".format(test_case+1, stack_list.pop()))

T = 10
for test_case in range(10):
    str_length = int(input())
    str_input = input()
    temp_stack = []
    postfix_stack = []

    for i in str_input:
        if i != '(' and i != ')' and i != '*' and i != '+':
            postfix_stack.append(int(i))
        elif i == '(':
            temp_stack.append('(')
        elif i == ')':
            while temp_stack[-1] != '(':
                postfix_stack.append(temp_stack.pop())
            temp_stack.pop()
        elif i == '*' or i == '+':
            flag = False
            while len(temp_stack) != 0:
                if i == '*':
                    if temp_stack[-1] == '*':
                        postfix_stack.append(temp_stack.pop())
                    else:
                        temp_stack.append('*')
                        flag = True
                        break
                elif i == '+':
                    if temp_stack[-1] == '*' or temp_stack[-1] == '+':
                        postfix_stack.append(temp_stack.pop())
                    else:
                        temp_stack.append('+')
                        flag = True
                        break
            if flag == False:
                temp_stack.append(i)
    for i in temp_stack:
        postfix_stack.append(i)
    
    for i in postfix_stack:
        if type(i) == type(1):
            temp_stack.append(i)
        else:
            s1 = temp_stack.pop()
            s2 = temp_stack.pop()
            if i == '+':
                temp_stack.append(s2+s1)
            else:
                temp_stack.append(s2*s1)
    print("#{0} {1}".format(test_case+1, temp_stack.pop()))

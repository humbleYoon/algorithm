T = int(input())

def reward_tracking(idx, c1, c2):
    global num, change_num
    global s
    global length, result

    num[c1], num[c2] = num[c2], num[c1]
    temp_reward = 0
    coif = 1
    for i in range(length):
        temp_reward += num[length-1-i]*coif
        coif *= 10
    
    if (idx, temp_reward) not in s:
        s.add((idx, temp_reward))
    else:
        num[c1], num[c2] = num[c2], num[c1]
        return None
    
    if idx >= change_num:
        if temp_reward > result:
            result = temp_reward
    else:
        for i in range(0, length-1):
            for j in range(i+1, length):
                reward_tracking(idx+1, i, j)
    
    num[c1], num[c2] = num[c2], num[c1]

for test_case in range(T):
    input_num, change_num = input().split()
    num = []
    for i in input_num:
        num.append(int(i))
    change_num = int(change_num)
    s = set()
    length = len(input_num)
    result = -989274844
    reward_tracking(0, 0, 0)
    print("#{0} {1}".format(test_case+1, result))
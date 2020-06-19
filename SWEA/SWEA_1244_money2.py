# 선택정렬로 최소한의 횟수로 숫자를 최대한 크게 만든 후, 맨 마지막 인덱스와 그 앞의 인덱스 자리를 바꾸는 것 반복
# 이 때 주의할 점은 선택정렬로 앞에서부터 자리를 정렬 시킬 때 그 자리에 있던 값이 제일 큰 값이면?
# 횟수를 줄이면 안된다! 교환이 이뤄지는 것으로 볼 수 없기 때문에

T = int(input())
for test_case in range(T):
    num, change_num = input().split()
    change_num = int(change_num)
    num_list = []
    num_len = 0
    for i in num:
        num_list.append(int(i))
        num_len += 1

    cnt = 0
    flag = False
    # 만약, 맥스값 같은게 앞에 더 있고, 인덱스의 절반 앞까지 자기보다 작은게 있다면? 맥스값들 중에 제일 앞에꺼랑 바꿔야 함
    # 반례가 너무 많다.. 테스트케이스 2번에서도 횟수 1, 2일 때 반례 발생..
    for i in range(num_len):
        num_max = num_list[i]
        max_idx = i
        for j in range(i+1, num_len):
            if num_max <= num_list[j]:
                num_max = num_list[j]
                max_idx = j
        
        if max_idx != i:
            cnt += 1
            temp = num_list[i]
            num_list[i] = num_list[max_idx]
            num_list[max_idx] = temp

        if cnt >= change_num:
            flag = True
            break
    
    if flag == False:
        for i in range(change_num-cnt):
            temp = num_list[num_len-1]
            num_list[num_len-1] = num_list[num_len-2]
            num_list[num_len-2] = temp

    result = 0
    pos = 10 ** (num_len-1)
    for i in num_list:
        result += i*pos
        pos = int(pos/10)

    print("#{0} {1}".format(test_case+1, result))
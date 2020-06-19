T = int(input())
for test_case in range(T):
    N, M = map(int, input().split()) # N: 화덕크기, M: 피자갯수
    pizza_list = list(map(int, input().split()))
    pizzaQueue = []
    cur_len = 0
    for i in range(N):
        pizzaQueue.append([pizza_list[cur_len], cur_len+1])
        cur_len += 1

    end_num = -1
    while pizzaQueue:
        current_pizza = pizzaQueue.pop(0)
        if current_pizza[0]//2 == 0:
            end_num = current_pizza[1]
            if cur_len < len(pizza_list):
                pizzaQueue.append([pizza_list[cur_len], cur_len+1])
                cur_len += 1
        else:
            pizzaQueue.append([current_pizza[0]//2, current_pizza[1]])
    
    print("#{0} {1}".format(test_case+1, end_num))
    
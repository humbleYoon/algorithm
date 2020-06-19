
T = int(input())
for test_case in range(T):
    cardnum_list = [0 for i in range(10)]
    N = int(input())
    card = input()
    max = -912718231
    max_idx = -1

    for i in card:
        num = int(i)
        cardnum_list[num] += 1

    for i in range(10):
        if cardnum_list[i] >= max:
            max = cardnum_list[i]
            max_idx = i

    print("#{0} {1} {2}".format(test_case+1, max_idx, max))
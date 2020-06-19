height_list = []
for i in range(9):
    height_list.append(int(input()))
height_list.sort()
height_sum = sum(height_list)
flag = False
for i in range(8):
    for j in range(i+1, 9):
        if height_sum - height_list[i] - height_list[j] == 100 and flag == False:
            flag = True
            for k in range(9):
                if k != i and k != j:
                    print(height_list[k])
                    
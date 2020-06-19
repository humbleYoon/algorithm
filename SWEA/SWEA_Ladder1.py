for test_case in range(10):
    testcase_num = int(input())
    map_list = []
    for i in range(100):
        row_list = list(map(int, input().split()))
        map_list.append(row_list)
    
    for i in range(100):
        if map_list[0][i] == 0:
            continue
        height = 0
        mv_pos = i
        while height < 100:
            flag = False
            if mv_pos-1 >= 0:
                if map_list[height][mv_pos-1] == 1:
                    left_pos = mv_pos-1
                    while map_list[height][left_pos] == 1:
                        left_pos -= 1
                        if left_pos == -1:
                            break
                    mv_pos = left_pos + 1
                    height += 1
                    flag = True

            if flag == False:
                if mv_pos+1 <= 99:
                    if map_list[height][mv_pos+1] == 1:
                        right_pos = mv_pos+1
                        while map_list[height][right_pos] == 1:
                            right_pos += 1
                            if right_pos == 100:
                                break
                        mv_pos = right_pos -1
                        height += 1
                        flag = True
            
            if flag == False:
                height += 1
        
        if map_list[height-1][mv_pos] == 2:
            print("#{0} {1}".format(testcase_num, i))
            break

# 선생님 코드
# 좌우 가로선을 살피고 사다리 올라가는 과정 구현한 부분이 심플

# def check(x, y):
#     if x < 0 or x > 99 : return False
#     if y < 0 or y > 99 : return False

#     if mat[x][y] : return True
#     else : return False

# def solve( ):
#     s = 0
#     while True:
#         if mat[99][s] == 2: break
#         s += 1

#     x = 99
#     y = s
#     d = 0       # -1(왼쪽), 0(위), 1(오른쪽)

#     while x != 0 :
#         if   ((d == 0 or d == -1) and check(x, y - 1)) : d = -1; y -= 1
#         elif ((d == 0 or d ==  1) and check(x, y + 1)) : d =  1; y +=1
#         else :	d = 0; x -= 1

#     return y;


# for tc in range(1, 11):
#     input()
#     mat = [0] * 100
#     for i in range(100):
#         mat[i] = list(map(int, input().split()))

#     print('#%d'%tc, solve( ))

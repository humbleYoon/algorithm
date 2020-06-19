# 깊이 15 안에는 도착 해야 함
# 가지가 4개씩 늘어나니까 다 돌리면 무조건 걸림
# 잘라내기 요소: 1. 나왔던 수는 가지 안내려도 됨
#               2. 백만 이상은 가지 안내려도 됨
# BFS로 트래킹 돌리면 1번 잘라내기에서 깊이는 고려하지 않아도 되고, 최소 연산 횟수 찾아내기도 쉽다
# 고려해야 하는건 메모리인데 깊이 20 안에는 답이 무조건 나오고
# 4^20 이면 무조건 터지겠지만, 맨 위에서부터 반은 잘라내고 시작한다고 보면
# 2^20 이므로 백만이니까 메모리 안터짐

import collections

CONST_INT_MAX = 1000000

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    checked = [False for i in range(CONST_INT_MAX+1)]
    d = collections.deque([])
    checked[N] = True
    d.append(N)
    depth = 0
    flag = False
    while d:
        temp_length = len(d)
        for i in range(temp_length):
            current = d.popleft()
            if current == M:
                flag = True
                break
            if 0 < current+1 <= CONST_INT_MAX and checked[current+1] == False:
                checked[current+1] = True
                d.append(current+1)
            if 0 < current-1 <= CONST_INT_MAX and checked[current-1] == False:
                checked[current-1] = True
                d.append(current-1)
            if 0 < current*2 <= CONST_INT_MAX and checked[current*2] == False:
                checked[current*2] = True
                d.append(current*2)
            if 0 < current-10 <= CONST_INT_MAX and checked[current-10] == False:
                checked[current-10] = True
                d.append(current-10)
        if flag == True:
            break
        depth += 1
    print("#{0} {1}".format(test_case+1, depth))
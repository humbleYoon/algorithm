# BFS => 시간 복잡도 O(V+E) 이므로 무조건 내에 들어오고..
import collections

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    checked = [False for i in range(N+1)]
    connected_info = [[] for i in range(N+1)]
    for i in range(M):
        f1, f2 = map(int, input().split())
        connected_info[f1].append(f2)
        connected_info[f2].append(f1)
    
    d = collections.deque([])
    checked[1] = True
    d.append(1)
    result = 0
    cnt = 0
    while d:
        temp_length = len(d)
        for i in range(temp_length):
            current = d.popleft()
            for j in connected_info[current]:
                if checked[j] == False:
                    checked[j] = True
                    d.append(j)
        result += len(d)
        cnt += 1
        if cnt == 2:
            break
    
    print("#{0} {1}".format(test_case+1, result))

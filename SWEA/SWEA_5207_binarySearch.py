T = int(input())
def binary_search(s, e, num):
    global N_list
    global result

    if N_list[s] > num:
        return None
    elif N_list[s] == num:
        
    

for test_case in range(T):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    N_list.sort()
    M_list = list(map(int, input().split()))
    result = 0
    for i in M_list:
        binary_search(0, N-1, i)
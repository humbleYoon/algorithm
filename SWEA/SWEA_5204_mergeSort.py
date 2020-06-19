T = int(input())

def merging(s1, e1, s2, e2):
    global N_list
    global result
    
    temp_list = []
    idx1 = s1
    idx2 = s2
    while idx1<=e1 and idx2<=e2:
        if N_list[idx1] <= N_list[idx2]:
            temp_list.append(N_list[idx1])
            idx1 += 1
        else:
            temp_list.append(N_list[idx2])
            idx2 += 1
    if idx1 > e1:
        while idx2 <= e2:
            temp_list.append(N_list[idx2])
            idx2 += 1
    else:
        result += 1
        while idx1 <= e1:
            temp_list.append(N_list[idx1])
            idx1 += 1
    for i in range(len(temp_list)):
        N_list[s1+i] = temp_list[i]

def mergeSort(s, e):
    # N_list의 s부터 e까지 병합정렬하는 함수

    global N_list
    
    if s >= e:
        return None
    else:
        mid = (s+e-1)//2
        mergeSort(s, mid)
        mergeSort(mid+1, e)
        merging(s, mid, mid+1, e)
        # N_list의 s부터 mid-1, mid부터 e까지의 구간을 합치는 함수


for test_case in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    result = 0
    mergeSort(0, N-1)
    print("#{0} {1} {2}".format(test_case+1, N_list[N//2], result))
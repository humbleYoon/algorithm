T = int(input())

def quickSort(myList, s, e):
    if s >= e:
        return None
    else:
        pivot = myList[s]
        low = s+1
        high = e
        while low <= high:
            while low<=high and myList[low]<=pivot:
                low += 1
            while low<=high and myList[high]>=pivot:
                high -= 1
            if low <= high:
                myList[low], myList[high] = myList[high], myList[low]    
        myList[s], myList[high] = myList[high], myList[s]
        quickSort(myList, s, high-1)
        quickSort(myList, high+1, e)

for test_case in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))

    # 1. quickSort(list, s1, e1) : list의 s1부터 e1까지 정렬하는 함수
    # 2. 기저조건 s1 >= e1 : 끝
    # 3. pivot을 정하고,
    # 4. low, high 인덱스를 양쪽에 두고 가운데로 수렴시킨다.
    # 5. low는 pivot보다 크면 멈추고, high는 pivot보다 작으면 멈춘다
    # 6. 서로 교환한다
    # 7. 교환 과정을 low와 high가 엇갈릴 때까지 반복한다
    # 8. high와 pivot을 교환한다.
    # 9. pivot의 위치는 정해졌고, pivot의 앞과 뒤를 quickSort 시킨다.
    # 이 방법으로 짜면 공간복잡도가 압도적으로 줄어든다. 시간복잡도는 조금 줄어들고.

    quickSort(N_list, 0, N-1)
    print("#{0} {1}".format(test_case+1, N_list[N//2]))
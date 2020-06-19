T = int(input())

for i in range(T):
    P, pa, pb = map(int, input().split())
    result = [0, 0]
    destination = [pa, pb]
    
    for j in range(2):
        start = 1
        end = P
        while start+1 <= end:
            mid = int((start+end)/2) # 파이썬에서는 나누면 소수로 나오기 때문에 int형으로 바꾸는 것 명심
            result[j] += 1
            if mid == destination[j]:
                break
            elif mid < destination[j]:
                start = mid
            else:
                end = mid
    
    if result[0] > result[1]:
        p_result = 'B'
    elif result[0] < result[1]:
        p_result = 'A'
    else:
        p_result = 0

    print("#{0} {1}".format(i+1, p_result))
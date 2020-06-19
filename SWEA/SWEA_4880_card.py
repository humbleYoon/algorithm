CONST_INT_MAX = 105

def fight(n1, n2):
    # N[n1]과 N[n2] 중 승자의 인덱스를 반환하는 함수
    global N_list

    if N_list[n1] == N_list[n2]:
            return n1
    else:
        if (N_list[n1]%3)+1 == N_list[n2]:
            return n2
        else:
            return n1

def DnC(start, end):
    # N[start] ~ N[end] 중 승자의 인덱스를 반환하는 함수
    if start + 1 >= end:
        return fight(start, end)
    else:
        mid = (start + end)//2
        return fight(DnC(start, mid), DnC(mid+1, end))
                
T = int(input())

for test_case in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    result = DnC(0, N-1) + 1
    print("#{0} {1}".format(test_case+1, result))
    
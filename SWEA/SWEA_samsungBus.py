CONST_INT_MAX = 5050

T = int(input())

for test_case in range(T):
    result = [0 for i in range(CONST_INT_MAX)]
    print("#{0} ".format(test_case+1), end='')
    N = int(input())
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            result[j] += 1
    P = int(input())
    for i in range(P):
        node = int(input())
        print("{0} ".format(result[node]), end='')
    print()
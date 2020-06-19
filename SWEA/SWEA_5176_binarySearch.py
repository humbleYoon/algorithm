T = int(input())

def num_save(node):
    global num, N
    global num_info

    if node*2 <= N:
        num_save(node*2)
    num_info[node] = num
    num += 1
    if node*2+1 <= N:
        num_save(node*2+1)

for test_case in range(T):
    N = int(input())
    num_info = [0 for i in range(N+1)]
    num = 1
    num_save(1)
    print("#{0} {1} {2}".format(test_case+1, num_info[1], num_info[N//2]))
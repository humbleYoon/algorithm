T = int(input())
data = []
num_pair = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for i in range(T):
    input().split()
    data.append(input().split())

for i in range(T):
    cnt = [0 for j in range(10)]
    for j in data[i]:
        if j == 'ZRO':
            cnt[0] += 1
        elif j == 'ONE':
            cnt[1] += 1
        elif j == 'TWO':
            cnt[2] += 1
        elif j == 'THR':
            cnt[3] += 1
        elif j == 'FOR':
            cnt[4] += 1
        elif j == 'FIV':
            cnt[5] += 1
        elif j == 'SIX':
            cnt[6] += 1
        elif j == 'SVN':
            cnt[7] += 1
        elif j == 'EGT':
            cnt[8] += 1
        elif j == 'NIN':
            cnt[9] += 1

    print("#{0}".format(i+1))
    for j in range(10):
        for k in range(cnt[j]):
            print("{0} ".format(num_pair[j]), end='')
    print()
T = int(input())
num_list = []
for __ in range(T):
    num_list.append(int(input()))

for t in range(T):
    while num_list[t]//10 > 0:
        temp_n = num_list[t]
        sum = 0
        while temp_n//10 > 0:
            sum += temp_n % 10
            temp_n = temp_n//10
        sum += temp_n
        num_list[t] = sum
    print("#{0} {1}".format(t+1, num_list[t]))
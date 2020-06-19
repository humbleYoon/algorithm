# result[idx]는 (idx+1)*10의 가로 크기를 갖는 직사각형을 채울 수 있는 경우의 수
# result[0], 즉 N = 10일 때 경우의 수는 1이다
# result[1], 즉 N = 20일 때 경우의 수는 3이다
# result[2], 즉 N = 30일 때 경우의 수는 N = 10인 상태에서 가로 크기 20인 직사각형을 채우는 경우의 수 + N = 20인 상태에서 가로 크기 10인 직사각형을 채우는 경우의 수
# 즉, result[0]*3 + result[1]*1이라 볼 수 있지만, 가로 크기 10인 직사각형이 모두 세로로 세워져 있는 경우는 중복이므로
# result[0]*2로 계산해줘야 한다
# result[n], 즉 N = (n+1)*10일 때 경우의 수는 result[n-2]*2 + result[n-1] 로 정의 할 수 있다. (n >= 2)

result = [0 for i in range(30)]
result[0] = 1 # N = 10
result[1] = 3 # N = 20

for i in range(2, 30):
    result[i] = result[i-2]*2 + result[i-1]

T = int(input())
for i in range(T):
    print("#{0} {1}".format(i+1, result[int(input())//10-1]))

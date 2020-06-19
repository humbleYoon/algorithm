# 한 타임당 우(혹은 좌)로 1, 상(혹은 하)로 1
# 좌우, 상하 길이 알면 타임 만큼 나누고, 그만큼 가면 끝

w, h = map(int, input().split())
start_x, start_y = map(int, input().split())
t = int(input())

direction_flag = True
if start_x == w:
    direction_flag = False
for i in range(t%(2*w)):
    if direction_flag == True:
        start_x += 1
    else:
        start_x -= 1

    if start_x == w:
        direction_flag = False
    elif start_x == 0:
        direction_flag = True

direction_flag = True
if start_y == h:
    direction_flag = False       
for i in range(t%(2*h)):
    if direction_flag == True:
        start_y += 1
    else:
        start_y -= 1

    if start_y == h:
        direction_flag = False
    elif start_y == 0:
        direction_flag = True

print("{0} {1}".format(start_x, start_y))
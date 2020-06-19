# 1: 북쪽 경계선, 2: 남쪽, 3: 서쪽, 4: 동쪽
# 1 or 2: 왼쪽으로부터의 거리, 3 or 4: 북쪽으로부터의 거리

width, height = map(int, input().split())
store_num = int(input())
store_info = []
result = 0
for i in range(store_num):
    pivot, distance = map(int, input().split())
    store_info.append([pivot, distance])
dong_pivot, dong_distance = map(int, input().split())

for i in store_info:
    if dong_pivot == i[0]:
        result += abs(dong_distance - i[1])
    elif (dong_pivot==1 and i[0]==2) or (dong_pivot==2 and i[0]==1) or (dong_pivot==3 and i[0]==4) or (dong_pivot==4 and i[0]==3):
        if dong_distance + height + i[1] < 2*width + 2*height - (dong_distance + height + i[1]):
            result += dong_distance + height + i[1]
        else:
            result += (2*width + 2*height - (dong_distance + height + i[1]))
    elif (dong_pivot==1 and i[0]==3) or (dong_pivot==1 and i[0]==4) or (dong_pivot==3 and i[0]==1) or (dong_pivot==3 and i[0]==2):
        result += (dong_distance + i[1])
        # 북쪽일 때 동, 서
        # 서쪽일 때 북, 남
    else:
        # 동쪽일 때 북, 남
        # 남쪽일 때 동, 서
        if dong_pivot == 4 and i[0] == 1:
            result += (dong_distance + (width-i[1]))
        elif dong_pivot == 4 and i[0] == 2:
            result += ((height-dong_distance) + (width-i[1]))
        elif dong_pivot == 2 and i[0] == 4:
            result += ((width-dong_distance) + (height-i[1]))
        else:
            result += (dong_distance + (height-i[1]))
print("{0}".format(result))
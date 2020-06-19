CONST_INT_MAX = 1050
map_list = [0 for i in range(CONST_INT_MAX)]

input_num = int(input())
max_idx = -1
height_max = -9887652434
end_idx = -1
for i in range(input_num):
    col, height = map(int, input().split())
    map_list[col] = height
    if height_max < height:
        max_idx = col
        height_max = height
    if end_idx < col:
        end_idx = col

result = 0
pivot_mx = 0
current_mx = 0
while current_mx <= max_idx:
    if map_list[pivot_mx] <= map_list[current_mx]:
        result += (current_mx-pivot_mx)*map_list[pivot_mx]
        pivot_mx = current_mx
    current_mx += 1

result += height_max

pivot_mx = end_idx
current_mx = end_idx
while current_mx >= max_idx:
    if map_list[pivot_mx] <= map_list[current_mx]:
        result += (pivot_mx-current_mx)*map_list[pivot_mx]
        pivot_mx = current_mx
    current_mx -= 1

print("{0}".format(result))

#   1 2 3 4 5 6 7
# 1 0 1 1 0 0 0 0
# 2
# 3
# 배열[1] = [2, 3]
# 배열[2] 
switch_num = int(input())
switch_list = list(map(int, input().split()))
student_num = int(input())

for i in range(student_num):
    student, take_num = map(int, input().split())
    if student == 1:
        temp_pos = 1
        while take_num*temp_pos <= switch_num:
            switch_list[take_num*temp_pos-1] = (switch_list[take_num*temp_pos-1]+1)%2
            temp_pos += 1
    else:
        switch_list[take_num-1] = (switch_list[take_num-1]+1)%2
        f_idx = take_num-2
        b_idx = take_num
        while f_idx >= 0 and b_idx < switch_num:
            if switch_list[f_idx] == switch_list[b_idx]:
                switch_list[f_idx] = (switch_list[f_idx]+1)%2
                switch_list[b_idx] = (switch_list[b_idx]+1)%2
                f_idx -= 1
                b_idx += 1
            else:
                break

temp_pos2 = 1
idx = 0
while idx < len(switch_list):
    print("{0} ".format(switch_list[idx]), end='')
    if (idx+1)%20==0:
        print()
    idx += 1

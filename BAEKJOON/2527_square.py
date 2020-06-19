T = 4

def xyStatus(x1, x2, x3, x4):
    if x1 > x4 or x2 < x3:
        return 0
    elif x1 == x4 or x2 == x3:
        return 1
    else:
        return 2

for test_case in range(T):
    # x끼리 떼어져있거나(0), 접해있거나(1), 겹쳐있거나(2)
    # y끼리 떼어져있거나, 접해있거나, 겹쳐있거나
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    x_status = xyStatus(x1, x2, x3, x4)
    y_status = xyStatus(y1, y2, y3, y4)
    
    # 겹치는 면적이 있을 때
    # 선 또는 점으로 접할 때
    # 아예 떨어져 있을 떄
    if x_status == 2 and y_status == 2:
        print("a")
    elif x_status == 1 and y_status == 1 :
        print("c")
    elif (x_status == 1 and y_status == 2) or (y_status == 1 and x_status == 2):
        print("b")
    else:
        print("d")
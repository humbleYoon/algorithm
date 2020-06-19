import math
T = 10
def inorder(node):
   global graph_info
   if graph_info[node][0] != '+' and graph_info[node][0] != '-' and graph_info[node][0] != '*' and graph_info[node][0] != '/':
       return int(graph_info[node][0])
   else:
       temp_left = inorder(graph_info[node][1])
       temp_right = inorder(graph_info[node][2])
       if graph_info[node][0] == '+':
           return temp_left + temp_right
       elif graph_info[node][0] == '-':
           return temp_left - temp_right
       elif graph_info[node][0] == '*':
           return temp_left * temp_right
       else:
           return temp_left / temp_right
for test_case in range(T):
   N = int(input())
   graph_info = [['', 0, 0] for i in range(N+1)]
   for i in range(N):
       temp_list = list(input().split())
       if len(temp_list) == 4:
           graph_info[int(temp_list[0])][0] += temp_list[1]
           graph_info[int(temp_list[0])][1] = int(temp_list[2])
           graph_info[int(temp_list[0])][2] = int(temp_list[3])
       elif len(temp_list) == 2:
           graph_info[int(temp_list[0])][0] += temp_list[1]
   print("#{0} {1}".format(test_case+1, math.trunc(inorder(1))))
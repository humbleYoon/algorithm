trans_char = [['0', '0000'], ['1', '0001'], ['2', '0010'], ['3', '0011'], ['4', '0100'], ['5', '0101'], ['6', '0110'], ['7', '0111'], ['8', '1000'], ['9', '1001'], ['A', '1010'], ['B', '1011'], ['C', '1100'], ['D', '1101'], ['E', '1110'], ['F', '1111']]

T = int(input())
for test_case in range(T):
    N, input_str = input().split()
    result = ""
    for i in range(int(N)):
        for j in range(16):
            if input_str[i] == trans_char[j][0]:
                result += trans_char[j][1]
                break
    print("#{0} {1}".format(test_case+1, result))
# https://www.acmicpc.net/problem/7682
import sys

def check_win(input_str, input_char):
    for i in range(0, 3):
        if input_str[i*3:i*3+3] == input_char*3:
            return True

    for i in range(0, 3):
        if input_str[i] + input_str[i+3] + input_str[i+6] == input_char*3:
            return True

    if input_str[0] + input_str[4] + input_str[8] == input_char*3:
        return True
    if input_str[2] + input_str[4] + input_str[6] == input_char*3:
        return True

    return False

while True:
    tmp_input = sys.stdin.readline().rstrip()
    if tmp_input == 'end':
        break

    x_cnt, o_cnt, blank_cnt = tmp_input.count('X'), tmp_input.count('O'), tmp_input.count('.')
    x_win, o_win = check_win(tmp_input, 'X'), check_win(tmp_input, 'O')
    if x_cnt == o_cnt:
        # o win
        if not x_win and o_win:
            print('valid')
        else:
            print('invalid')
    elif x_cnt == o_cnt + 1:
        # x win
        if x_win and not o_win:
            print('valid')
        # draw
        elif x_cnt == 5 and o_cnt == 4 and not x_win and not o_win:
            print('valid')

        else:
            print('invalid')
    else:
        print('invalid')
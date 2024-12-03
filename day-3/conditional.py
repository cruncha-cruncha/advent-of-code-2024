# problem 2
import re

def is_numeric(s):
    return s == '0' or s == '1' or s == '2' or s == '3' or s == '4' or s == '5' or s == '6' or s == '7' or s == '8' or s == '9'

def fsm(text):
    # state
    enable = 0
    disable = 0
    mul = 0

    track_mul = True
    mul_num_buffer = ["",""]

    mul_buffer = []
    
    chars = list(text)
    for c in chars:
        if track_mul:
            if c == 'm':
                mul = 1
            elif mul == 1 and c == 'u':
                mul = 2
            elif mul == 2 and c == 'l':
                mul = 3
            elif mul == 3 and c == '(':
                mul = 4
            elif mul == 4 and is_numeric(c):
                mul = 5
                mul_num_buffer[0] = ""
                mul_num_buffer[0] += c
            elif mul == 5 and is_numeric(c):
                mul = 5
                mul_num_buffer[0] += c
            elif mul == 5 and c == ',' and len(mul_num_buffer[0]) <= 3:
                mul = 6
            elif mul == 6 and is_numeric(c):
                mul = 7
                mul_num_buffer[1] = ""
                mul_num_buffer[1] += c
            elif mul == 7 and is_numeric(c):
                mul = 7
                mul_num_buffer[1] += c
            elif mul == 7 and c == ')' and len(mul_num_buffer[1]) <= 3:
                mul_buffer.append(tuple(mul_num_buffer.copy()))
                mul = 0
            else:
                mul = 0

            if c == 'd':
                disable = 1
            elif disable == 1 and c == 'o':
                disable = 2
            elif disable == 2 and c == 'n':
                disable = 3
            elif disable == 3 and c == '\'':
                disable = 4
            elif disable == 4 and c == 't':
                disable = 5
            elif disable == 5 and c == '(':
                disable = 6
            elif disable == 6 and c == ')':
                track_mul = False
                disable = 0
            else:
                disable = 0

        else:
            if c == 'd':
                enable = 1
            elif enable == 1 and c == 'o':
                enable = 2
            elif enable == 2 and c == '(':
                enable = 3
            elif enable == 3 and c == ')':
                track_mul = True
                enable = 0
            else:
                enable = 0

    return mul_buffer
            
def main():
    text = ""
    with open('input.txt') as f:
        text = f.read()

    matches = fsm(text)
    good_commands = sum([int(x) * int(y) for x, y in matches])
    print(good_commands)

if __name__ == '__main__':
    main()


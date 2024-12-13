# problem 1

import re

def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def compute_lcm(x, y):
   return (x*y)//compute_gcd(x,y)

def main():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    equations = []
    a_x, a_y, b_x, b_y = 0, 0, 0, 0
    for i, line in enumerate(lines):
        if line.startswith('Button A:'):
            match_string = "Button A: X\+(\d+), Y\+(\d+)"
            groups = re.match(match_string, line).groups()
            a_x = int(groups[0])
            a_y = int(groups[1])
        elif line.startswith('Button B:'):
            match_string = "Button B: X\+(\d+), Y\+(\d+)"
            groups = re.match(match_string, line).groups()
            b_x = int(groups[0])
            b_y = int(groups[1])
        elif line.startswith('Prize:'):
            match_string = "Prize: X=(\d+), Y=(\d+)"
            groups = re.match(match_string, line).groups()
            p_x = int(groups[0])
            p_y = int(groups[1])
            equations.append(((p_x, a_x, b_x), (p_y, a_y, b_y)))

    solved = []
    for i, eq in enumerate(equations):
        eq_1 = eq[0]
        eq_2 = eq[1]
        a_lcm = compute_lcm(eq_1[1], eq_2[1])
        coef_1 = a_lcm // eq_1[1]
        coef_2 = a_lcm // eq_2[1]
        eq_1 = (eq_1[0] * coef_1, eq_1[1] * coef_1, eq_1[2] * coef_1)
        eq_2 = (eq_2[0] * coef_2 - eq_1[0], 0, eq_2[2] * coef_2 - eq_1[2])
        if eq_2[0] % eq_2[2] == 0:
            b = eq_2[0] // eq_2[2]
            a = (eq_1[0] - eq_1[2] * b) // eq_1[1]
            solved.append((i, a, b))

    total_cost = 0
    for sol in solved:
        i, a, b = sol
        total_cost += a * 3 + b

    print(total_cost)

if __name__ == '__main__':
    main()

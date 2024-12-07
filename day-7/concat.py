# problem 2

def parse_line(line):
    words = line.split()
    return (int(words[0][:-1]), [int(w) for w in words[1:]])

def can_equate(val, nums):
    test_num = 0
    operators = ['+', '*', '||']
    operations = [0 for x in nums[1:]]
    while test_num < 3**len(operations):
        # convert to base three
        quotient = test_num
        for i in range(len(operations)):
            operations[i] = quotient % 3
            quotient = quotient // 3

        result = nums[0]
        for i, o in enumerate(operations):
            if operators[o] == '+':
                result += nums[i+1]
            elif operators[o] == '*':
                result *= nums[i+1]
            elif operators[o] == '||':
                result = result * 10**len(str(nums[i+1]))
                result += nums[i+1]
            
        if result == val:
            return True
        test_num += 1
        
    return False

def main():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    sum = 0
    for line in lines:
        val, nums = parse_line(line)
        if can_equate(val, nums):
            sum += val

    print(sum)
  
if __name__ == '__main__':
    main()
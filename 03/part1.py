import re

# must match mult(xxx, yyy), examples: mul(667,142),mul(818,66)
mul_regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


if __name__ == '__main__':
    data = read_input()
    result = sum(int(x)*int(y) for x, y in mul_regex.findall(data))
    print("Result:", result)
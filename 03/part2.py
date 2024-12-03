from part1 import read_input, mul_regex
import re

# must match "do()" and "don't()"
do_regex = re.compile(r"do(n't)?\(\)")

if __name__ == '__main__':
    data = read_input()

    # get do matches
    do_matches = do_regex.finditer(data)
    do_match_indices = {do_match.start(): do_match.group() for do_match in do_matches}

    # get mult matches
    mult_matches = mul_regex.finditer(data)
    mult_match_indices = {mult_match.start(): mult_match.groups() for mult_match in mult_matches}

    all_matches = {**do_match_indices, **mult_match_indices}
    result = 0
    do = True
    for match in sorted(all_matches.keys()):
        if all_matches[match] == "do()":
            do = True
        elif all_matches[match] == "don't()":
            do = False
        elif do:
            x, y = all_matches[match]
            result += int(x) * int(y)

    print("Result:", result)
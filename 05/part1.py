def load_file(file_path: str) -> str:
    """
    Example file:

    47|53
    97|13
    97|61
    97|47
    75|29
    61|13
    75|53
    29|13
    97|29
    53|29
    61|53
    97|53
    61|29
    47|13
    75|47
    97|75
    47|61
    75|61
    47|29
    75|13
    53|13

    75,47,61,53,29
    97,61,53,29,13
    75,29,13
    75,97,47,61,53
    61,13,29
    97,13,75,29,47
    """
    with open(file_path, "r") as file:
        # parse first part of the file (till double newline)
        first_part_lines = []
        for line in file:
            if line == "\n":
                break
            first_part_lines += [line]
        
        first_part = [tuple(map(int, line.split("|"))) for line in first_part_lines]

        # parse second part of the file (till end of file)
        second_part= []
        for line in file:
            second_part.append([int(x) for x in line.split(",")])

    return first_part, second_part


def check_update(update: list, instructions: list) -> bool:
    """
    Check if the update is valid according to the instructions.
    """
    for instruction in instructions:
        if instruction[0] in update and instruction[1] in update:
            if update.index(instruction[0]) > update.index(instruction[1]):
                return False

    return True


if __name__ == '__main__':
    instructions, updates = load_file("input.txt")
    print("Instructions:")
    print(instructions)

    result = 0
    for update in updates:
        if check_update(update, instructions):
            print("Valid update: ", update)

            # add the median number of the update list
            result += update[len(update) // 2]

    print("Result:", result)

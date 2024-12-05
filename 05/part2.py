from part1 import load_file, check_update

def fix_update(update: list, instructions: list) -> list:
    """
    Fix the update according to the instructions.
    """

    applicable_instructions = [instruction for instruction in instructions if instruction[0] in update and instruction[1] in update]

    while not check_update(update, instructions):
        for instruction in applicable_instructions:
                if update.index(instruction[0]) > update.index(instruction[1]):
                    # swap the elements
                    update[update.index(instruction[0])], update[update.index(instruction[1])] = update[update.index(instruction[1])], update[update.index(instruction[0])]
        
    assert check_update(update, instructions), update
    return update

if __name__ == '__main__':
    instructions, updates = load_file("input.txt")


    # find the incorrect updates
    result = 0
    for update in updates:
        if not check_update(update, instructions):
            print("\nIncorrect update:", update)

            fixed_update = fix_update(update, instructions)

            print("Fixed update:", fixed_update)

            # add the median number of the update list
            result += fixed_update[len(update) // 2]


    print("\n\nResult:", result)
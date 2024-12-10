from itertools import product


def load_file(input_file: str) -> dict[int, list[int]]:

    operations = []

    # must split each row by colon, and the second half after colon by space, convert the second half list to int
    with open(input_file, "r") as file:
        lines = [line.strip() for line in file.readlines()]
        for line in lines:
            result, _, operands = line.partition(":")
            operands = [int(x) for x in operands.split()]

            operations.append((int(result), operands))

    return operations


def eval_left_to_right(operands: list[str], operators: list[str]) -> int:
    total = operands[0]
    for operand, operator in zip(operands[1:], operators):
        if operator == "+":
            total = total + operand
        elif operator == "*":
            total = total * operand
        elif operator == "||":
            total = int(str(total) + str(operand))
        else:
            raise ValueError("Invalid operator")

    return total


def validate_operation(result: int, operands: list[int], operators: list[str]) -> bool:

    for operator_set in product(operators, repeat=len(operands) - 1):
        if result == eval_left_to_right(operands, operator_set):
            return True, operator_set

    return False, None


def compute_total(operator_set: list[str]) -> None:
    operations = load_file("input.txt")
    print(operations)

    total = 0
    for result, operands in operations:
        valid, operators = validate_operation(result, operands, operator_set)
        if valid:
            expression = (
                "".join(f"{x} {y} " for x, y in zip(operands, operators))
                + f"{operands[-1]}"
            )
            print(f"Operation with {result} = {expression} is valid")
            total += result

    print("Total:", total)


if __name__ == "__main__":
    compute_total(["+", "*"])

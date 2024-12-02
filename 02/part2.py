from part1 import read_file, is_safe

def is_safe_without_one(report):
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_safe(new_report):
            return True
    return False

if __name__ == "__main__":
    reports = read_file()

    safe_count = 0
    for report in reports:
        if res := is_safe(report):
            safe_count += 1
        elif is_safe_without_one(report):
            safe_count += 1
        # print(res)

    print("Safe count:", safe_count)
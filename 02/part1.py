# read file
def read_file():
    reports = []
    with open("input.txt") as f:
        rows = f.read().splitlines()
        for report in rows:
            values = [int(x) for x in report.split()]
            reports.append(values)
    return reports

def is_safe(report):

    tolerated_already = False
    # decreasing
    if report[0] > report[1]:
        
        for x in range(1, len(report)):
            # print(report[x - 1], report[x], report[x] + 3 >= report[x - 1], report[x - 1] >= report[x] + 1)
            if not (report[x] + 3 >= report[x - 1] >= report[x] + 1):
                return False

        return True

    # increasing
    elif report[0] < report[1]:
        
        for x in range(1, len(report)):
            # print(report[x - 1], report[x], report[x] + 3 <= report[x], report[x] >= report[x - 1] + 1)

            if not (report[x - 1] + 1 <= report[x] <= report[x - 1] + 3):
                return False


        return True

    else:
        return False

    

if __name__ == "__main__":
    reports = read_file()

    safe_count = 0
    for report in reports:
        if res := is_safe(report):
            safe_count += 1
        # print(res)

    print("Safe count:", safe_count)
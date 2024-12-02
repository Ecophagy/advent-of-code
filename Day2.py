
def read_data():
    reports = []
    with open("input/Day2.txt") as f:
        lines = f.readlines()
        for line in lines:
            raw_report = line.split(" ")
            report = []
            for raw_level in raw_report:
                report.append(int(raw_level))
            reports.append(report)
    return reports

def report_safe(report):
    report_is_safe = True

    # Check order is correct (all ascending or descending)
    for i in range(1, len(report) - 1):
        if (report[i-1] < report[i] and report[i] > report[i+1]) or (report[i-1] > report[i] and report[i] < report[i+1]):
            return False

    # Check id difference between adjacent elements is > 3 or < 1
    for i in range(1, len(report)):
        if abs(report[i - 1] - report[i]) < 1 or abs(report[i - 1] - report[i]) > 3:
            return False

    return report_is_safe

# Part 1
def count_safe_reports(reports):
    safe_reports = 0
    for report in reports:
        safe_report = report_safe(report)
        if safe_report:
            safe_reports = safe_reports + 1

    print(f"Safe Reports: {safe_reports}")

# Part 2
def count_tolerant_safe_reports(reports):
    safe_reports = 0
    for report in reports:
        safe_report = report_safe(report)
        if safe_report:
            safe_reports = safe_reports + 1
        else:
            # Try again removing each index. Brute force solution!
            for i in range(0, len(report)):
                x = report.pop(i)
                safe_report = report_safe(report)
                if safe_report:
                    safe_reports = safe_reports + 1
                    break
                else:
                    # Removing that index did not make the sequence safe, so reinsert and try again
                    report.insert(i, x)

    print(f"Tolerant Safe Reports: {safe_reports}")


if __name__ == "__main__":
    reports = read_data()
    count_safe_reports(reports)
    count_tolerant_safe_reports(reports)
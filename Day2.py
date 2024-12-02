

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

def count_safe_reports(reports):
    safe_reports = 0
    for report in reports:
        report_safe = True
        descending = report[0] - report[1] > 0
        for i in range(1, len(report)):
            if abs(report[i - 1] - report[i]) < 1 or abs(report[i - 1] - report[i]) > 3:
                report_safe = False
                break
            if descending:
                report_safe = report[i-1] > report[i]
            else:
                report_safe = report[i-1] < report[i]
            if not report_safe:
                break
        if report_safe:
            safe_reports = safe_reports + 1

    print(f"Safe Reports: {safe_reports}")


if __name__ == "__main__":
    reports = read_data()
    count_safe_reports(reports)
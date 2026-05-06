
def build_clickbait_report(rows):
    report = []
    for row in rows:
        ctr = float(row["ctr"])
        retention_rate = float(row["retention_rate"])

        if ctr > 15 and retention_rate < 40:
            report.append({
                "title": row["title"],
                "ctr": ctr,
                "retention_rate": retention_rate,
            })

    report.sort(key=lambda x: x["ctr"], reverse=True)
    return report


REPORTS = {
    "clickbait": build_clickbait_report,
}

def build_report(report_name, rows):
    try:
        report_builder = REPORTS[report_name]

        return report_builder(rows)
    except KeyError:
        raise KeyError(f"Report {report_name} not found")
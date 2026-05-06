import argparse
import csv
from .reports import build_clickbait_report, build_report

from tabulate import tabulate


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
    )

    parser.add_argument(
        "--report",
        required=True,
    )

    return parser.parse_args()

def read_csv(file_paths):
    rows = []

    for file_path in file_paths:
        with open(file_path, encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                rows.append(row)
    return rows



def main():
    args = parse_args()

    rows = read_csv(args.files)
    report = build_report(args.report, rows)

    print(tabulate(report, headers="keys", tablefmt="github"))

if __name__ == "__main__":
    main()
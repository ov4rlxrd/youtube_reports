import pytest


from youtube_reports.main import read_csv
from youtube_reports.reports import build_clickbait_report, build_report





def test_build_clickbait_report_filter():
    rows = [
        {
            "title": "1",
            "ctr": "18.2",
            "retention_rate": "35",
        },
        {
            "title": "2",
            "ctr": "10.0",
            "retention_rate": "20",
        },
        {
            "title": "3",
            "ctr": "20.0",
            "retention_rate": "80",
        },
    ]

    result = build_clickbait_report(rows)

    assert result == [
        {
            "title": "1",
            "ctr": 18.2,
            "retention_rate": 35,
        }

    ]


def test_build_clickbait_report_strict():
    rows = [
        {
            "title": "1",
            "ctr": "15",
            "retention_rate": "30",
        },
        {
            "title": "2",
            "ctr": "20",
            "retention_rate": "40",
        },
        {
            "title": "Valid",
            "ctr": "15.1",
            "retention_rate": "39.9",
        },
    ]
    result = build_clickbait_report(rows)

    assert len(result) == 1
    assert result[0]["title"] == "Valid"


def test_build_clickbait_report_sort():
    rows = [
        {
            "title": "1",
            "ctr": "18.0",
            "retention_rate": "30",
        },
        {
            "title": "2",
            "ctr": "25.0",
            "retention_rate": "20",
        },
        {
            "title": "3",
            "ctr": "21.0",
            "retention_rate": "35",
        },
    ]

    result = build_clickbait_report(rows)

    assert [row["title"] for row in result] == [
        "2",
        "3",
        "1"
    ]

def test_build_report_error():
    with pytest.raises(KeyError):
        build_report("---", [])


def test_read_csv_error():
    with pytest.raises(FileNotFoundError):
        read_csv("test.csv")
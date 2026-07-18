import csv
import sys
from collections import defaultdict


def correlation_key(row):
    return f'{row["signal"]}:{row["region"]}'


def clusters(rows):
    grouped = defaultdict(list)
    for row in rows:
        grouped[correlation_key(row)].append(row["incident_id"])
    return [
        {"key": key, "incident_ids": incident_ids, "count": len(incident_ids)}
        for key, incident_ids in sorted(grouped.items())
        if len(incident_ids) > 1
    ]


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for item in clusters(csv.DictReader(handle)):
            print(f'{item["key"]}: { ",".join(item["incident_ids"]) }')


if __name__ == "__main__":
    main(sys.argv[1])
